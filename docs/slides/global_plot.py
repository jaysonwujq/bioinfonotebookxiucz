
    def global_plot(self):
        chroms = []
        for c, (l, t) in self.reference_genome["chromosomes"].items():
            rd_chr = self.io[self.plot_files[0]].rd_chromosome_name(c)
            if (len(self.chrom) == 0 or (rd_chr in self.chrom) or (c in self.chrom)) and rd_chr is not None:
                if (Genome.is_autosome(c) or Genome.is_sex_chrom(c)):
                    chroms.append((rd_chr, l))
        panels = self.panels
        bin_size = self.bin_size
        snp_flag = (FLAG_USEMASK if self.snp_use_mask else 0) | (FLAG_USEID if self.snp_use_id else 0) | (
            FLAG_USEHAP if self.snp_use_phase else 0)
        rd_flag = (FLAG_USEMASK if self.rd_use_mask else 0) | (FLAG_GC_CORR if self.rd_use_gc_corr else 0)
        n = len(self.plot_files)
        self.new_figure(panel_count=n)
        for ii in range(len(self.plot_files)):
            ix = self.plot_files[ii]
            self.new_subgrid(len(panels), hspace=0.05, wspace=0.05)
            io = self.io[ix]
            for i in range(len(panels)):
                ax = self.next_subpanel(sharex=True)
                if i == 0 and self.title:
                    ax.set_title(self.file_title(ix), position=(0.01, 0.9),
                                 fontdict={'verticalalignment': 'top', 'horizontalalignment': 'left'},
                                 color='C0')

                if panels[i] == "rd":
                    start = 0
                    xticks = [0]
                    xticks_minor = []
                    xticks_labels = []
                    for c, l in chroms:
                        mean, stdev = io.rd_normal_level(bin_size, rd_flag | FLAG_GC_CORR)
                        his_p = io.get_signal(c, bin_size, "RD", rd_flag)
                        pos = range(start, start + len(his_p))
                        if self.markersize == "auto":
                            plt.plot(pos, his_p, ls='', marker='.', markersize=1)
                        else:
                            plt.plot(pos, his_p, ls='', marker='.', markersize=self.markersize)
                        xticks_minor.append(start + len(his_p) // 2)
                        xticks_labels.append(Genome.canonical_chrom_name(c))
                        start += l // bin_size + 1
                        xticks.append(start)

                    ax.set_xlim([0, start])
                    ax.xaxis.set_ticks(xticks)
                    ax.xaxis.set_ticklabels([""] * len(xticks))
                    if i == (len(panels) - 1):
                        ax.xaxis.set_ticks(xticks_minor, minor=True)
                        ax.xaxis.set_ticklabels(xticks_labels, minor=True)
                    else:
                        plt.setp(ax.get_xticklabels(which="both"), visible=False)
                    yticks = np.arange(self.rd_manhattan_range[0], self.rd_manhattan_range[1], 0.5)
                    ax.yaxis.set_ticklabels([str(int(2 * t)) for t in yticks])
                    ax.yaxis.set_ticks(yticks * mean)
                    ax.set_ylabel("RD [CN]")
                    ax.set_ylim([self.rd_manhattan_range[0] * mean, self.rd_manhattan_range[1] * mean])
                    ax.grid()
                    self.fig.add_subplot(ax)

                elif panels[i] == "snp":
                    start = 0
                    xticks = []
                    xticks_minor = []
                    xticks_labels = []
                    pos_x = []
                    for c, l in chroms:
                        pos, ref, alt, nref, nalt, gt, flag, qual = io.read_snp(c)
                        ix = 0
                        hpos = []
                        color = []
                        alpha = 0.7
                        baf = []
                        while ix < len(pos):
                            if (nref[ix] + nalt[ix]) != 0 and ((not self.snp_use_id) or (flag[ix] & 1)):
                                hpos.append(start + (pos[ix] / bin_size))
                                if gt[ix] % 4 != 2:
                                    baf.append(1.0 * nalt[ix] / (nref[ix] + nalt[ix]))
                                else:
                                    baf.append(1.0 * nref[ix] / (nref[ix] + nalt[ix]))
                                if self.snp_alpha_P:
                                    alpha = None
                                    color.append(
                                        colors.to_rgba(self.snp_colors[(gt[ix] % 4) * 2 + 1], (flag[ix] >> 1) * 0.4))
                                else:
                                    color.append(self.snp_colors[(gt[ix] % 4) * 2 + (flag[ix] >> 1)])
                            ix += 1
                        if self.markersize == "auto":
                            ax.scatter(hpos, baf, marker='.', edgecolor=color, c=color, s=0.1, alpha=alpha)
                        else:
                            ax.scatter(hpos, baf, marker='.', edgecolor=color, c=color, s=self.markersize, alpha=alpha)
                        xticks_minor.append(start + l // bin_size // 2)
                        xticks_labels.append(Genome.canonical_chrom_name(c))
                        start += l // bin_size + 1
                        xticks.append(start)
                    ax.set_xlim([0, start])
                    ax.xaxis.set_ticks(xticks)
                    ax.xaxis.set_ticklabels([""] * len(xticks))
                    if i == (len(panels) - 1):
                        ax.xaxis.set_ticks(xticks_minor, minor=True)
                        ax.xaxis.set_ticklabels(xticks_labels, minor=True)
                    else:
                        plt.setp(ax.get_xticklabels(minor=True), visible=False)
                    ax.grid()
                    ax.yaxis.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
                    ax.yaxis.set_ticklabels(["0", "1/4", "1/2", "3/4", "1"])
                    ax.set_ylabel("BAF")
                    ax.set_ylim([-0.05, 1.05])
                    ax.yaxis.grid()
                    self.fig.add_subplot(ax)

                elif panels[i] == "snv" or panels[i][:4] == "snv:":
                    callset = "default"
                    if panels[i][:4] == "snv:":
                        callset = panels[i].split(":")[1]
                    start = 0
                    xticks = []
                    xticks_minor = []
                    xticks_labels = []
                    pos_x = []
                    for c, l in chroms:
                        pos, ref, alt, nref, nalt, gt, flag, qual = io.read_snp(c, callset=callset)
                        ix = 0
                        hpos = []
                        color = []
                        alpha = 0.7
                        baf = []
                        while ix < len(pos):
                            if (nref[ix] + nalt[ix]) != 0 and ((not self.snp_use_id) or (flag[ix] & 1)):
                                hpos.append(start + (pos[ix] / bin_size))
                                if gt[ix] % 4 != 2:
                                    baf.append(1.0 * nalt[ix] / (nref[ix] + nalt[ix]))
                                else:
                                    baf.append(1.0 * nref[ix] / (nref[ix] + nalt[ix]))
                                if self.snp_alpha_P:
                                    alpha = None
                                    color.append(
                                        colors.to_rgba(self.snp_colors[(gt[ix] % 4) * 2 + 1], (flag[ix] >> 1) * 0.4))
                                else:
                                    color.append(self.snp_colors[(gt[ix] % 4) * 2 + (flag[ix] >> 1)])
                            ix += 1
                        if self.markersize == "auto":
                            ax.scatter(hpos, baf, marker='.', edgecolor=color, c=color, s=0.1, alpha=alpha)
                        else:
                            ax.scatter(hpos, baf, marker='.', edgecolor=color, c=color, s=self.markersize, alpha=alpha)
                        xticks_minor.append(start + l // bin_size // 2)
                        xticks_labels.append(Genome.canonical_chrom_name(c))
                        start += l // bin_size + 1
                        xticks.append(start)
                    ax.set_xlim([0, start])
                    ax.xaxis.set_ticks(xticks)
                    ax.xaxis.set_ticklabels([""] * len(xticks))
                    if i == (len(panels) - 1):
                        ax.xaxis.set_ticks(xticks_minor, minor=True)
                        ax.xaxis.set_ticklabels(xticks_labels, minor=True)
                    else:
                        plt.setp(ax.get_xticklabels(minor=True), visible=False)
                    ax.grid()
                    ax.yaxis.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
                    ax.yaxis.set_ticklabels(["0", "1/4", "1/2", "3/4", "1"])
                    ax.set_ylabel("BAF")
                    ax.set_ylim([-0.05, 1.05])
                    ax.yaxis.grid()
                    self.fig.add_subplot(ax)


                elif panels[i] == "likelihood":
                    start = 0
                    xticks = [0]
                    xticks_minor = []
                    xticks_labels = []
                    gl = []
                    for c, l in chroms:
                        likelihood = io.get_signal(c, bin_size, "SNP likelihood", snp_flag)
                        lh = list(likelihood)
                        size = l // bin_size + 1
                        if len(lh) < size:
                            if len(lh) > 0:
                                lh.extend([lh[-1] for jj in range(size - len(lh))])
                            elif len(gl) > 0:
                                lh.extend([gl[-1] for jj in range(size - len(lh))])

                        gl.extend(lh)
                        xticks_minor.append(start + l // bin_size // 2)
                        xticks_labels.append(Genome.canonical_chrom_name(c))
                        start += l // bin_size + 1
                        xticks.append(start)

                    img = np.array(gl).transpose()
                    img[0, :] = 0
                    img[-1, :] = 0
                    ax.imshow(img, aspect='auto')
                    ax.yaxis.set_ticks([0, img.shape[0] / 4, img.shape[0] / 2, 3 * img.shape[0] / 4, img.shape[0] - 1],
                                       minor=[])
                    ax.yaxis.set_ticklabels(["1", "3/4", "1/2", "1/4", "0"])
                    ax.set_ylabel("BAF")
                    ax.set_xlim([0, start])
                    ax.xaxis.set_ticks(xticks)
                    ax.xaxis.set_ticklabels([""] * len(xticks))
                    if i == (len(panels) - 1):
                        ax.xaxis.set_ticks(xticks_minor, minor=True)
                        ax.xaxis.set_ticklabels(xticks_labels, minor=True)
                    else:
                        plt.setp(ax.get_xticklabels(minor=True), visible=False)
                    ax.xaxis.grid()
                    self.fig.add_subplot(ax)

        self.fig_show(suffix="global")

 