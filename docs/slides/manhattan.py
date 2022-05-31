
    def manhattan(self, plot_type="rd"):
        bin_size = self.bin_size
        if self.reference_genome is None:
            _logger.warning("Missing reference genome required for manhattan.")
            return
        n = len(self.plot_files)
        ix = self.plot_files

        self.new_figure(panel_count=n, grid=(1, n), panel_size=(24, 2))
        for i in range(n):
            ax = self.next_panel()
            io = self.io[ix[i]]
            ax.set_title(self.file_title(ix[i]), position=(0.01, 1.01),
                         fontdict={'verticalalignment': 'bottom', 'horizontalalignment': 'left'})

            if plot_type == "rd":
                chroms = []
                for c, (l, t) in self.reference_genome["chromosomes"].items():
                    rd_chr = io.rd_chromosome_name(c)
                    if len(self.chrom) == 0 or (rd_chr in self.chrom) or (c in self.chrom):
                        if io.signal_exists(rd_chr, bin_size, "RD", 0) and \
                                io.signal_exists(rd_chr, bin_size, "RD", FLAG_GC_CORR) and \
                                (Genome.is_autosome(c) or Genome.is_sex_chrom(c)):
                            chroms.append((rd_chr, l))

                apos = 0
                xticks = [0]

                max_m, stdev = io.rd_normal_level(bin_size, FLAG_GC_CORR)
                for c, l in chroms:
                    flag_rd = (FLAG_USEMASK if self.rd_use_mask else 0)
                    his_p = io.get_signal(c, bin_size, "RD", flag_rd)
                    his_p_corr = io.get_signal(c, bin_size, "RD", flag_rd | FLAG_GC_CORR)
                    if self.rd_manhattan_call:
                        his_p_call = io.get_signal(c, bin_size, "RD call", flag_rd | FLAG_GC_CORR)
                        his_p_mosaic_seg = io.get_signal(c, bin_size, "RD mosaic segments",
                                                         flag_rd | FLAG_GC_CORR)
                        his_p_mosaic_seg = segments_decode(his_p_mosaic_seg)
                        his_p_mosaic_call = io.get_signal(c, bin_size, "RD mosaic call",
                                                          flag_rd | FLAG_GC_CORR)
                        his_p_mosaic_seg_2d = io.get_signal(c, bin_size, "RD mosaic segments 2d",
                                                            flag_rd | FLAG_GC_CORR)
                        his_p_mosaic_seg_2d = segments_decode(his_p_mosaic_seg_2d)
                        his_p_mosaic_call_2d = io.get_signal(c, bin_size, "RD mosaic call 2d",
                                                             flag_rd | FLAG_GC_CORR)
                        his_p_mosaic = np.zeros_like(his_p) * np.nan
                        if his_p_mosaic_call is not None and len(his_p_mosaic_call) > 0 and (
                                "rd_mosaic" in self.callers):
                            for seg, lev in zip(list(his_p_mosaic_seg), list(his_p_mosaic_call[0])):
                                for segi in seg:
                                    his_p_mosaic[segi] = lev
                        his_p_mosaic_2d = np.zeros_like(his_p) * np.nan
                        if his_p_mosaic_call_2d is not None and len(
                                his_p_mosaic_call_2d) > 0 and ("combined_mosaic" in self.callers):
                            for seg, lev in zip(list(his_p_mosaic_seg_2d), list(his_p_mosaic_call_2d[0])):
                                for segi in seg:
                                    his_p_mosaic_2d[segi] = lev
                    pos = range(apos, apos + len(his_p))
                    ax.text(apos + len(his_p) // 2, max_m // 10, Genome.canonical_chrom_name(c),
                            fontsize=8, verticalalignment='bottom', horizontalalignment='center', )
                    if self.markersize == "auto":
                        plt.plot(pos, his_p_corr, ls='', marker='.')
                    else:
                        plt.plot(pos, his_p_corr, ls='', marker='.', markersize=self.markersize)
                    if self.rd_manhattan_call:
                        if his_p_call is not None and len(his_p_call) > 0 and ("rd_mean_shift" in self.callers):
                            plt.step(pos, his_p_call, "r")
                        if his_p_mosaic_call is not None and len(his_p_mosaic_call) > 0 and (
                                "rd_mosaic" in self.callers):
                            plt.plot(pos, his_p_mosaic, "k")
                        if his_p_mosaic_call_2d is not None and len(
                                his_p_mosaic_call_2d) > 0 and ("combined_mosaic" in self.callers):
                            plt.plot(pos, his_p_mosaic_2d, "k")
                    apos += len(his_p)
                    xticks.append(apos)
                ax.xaxis.set_ticklabels([])
                ax.yaxis.set_ticklabels([])
                ax.yaxis.set_ticks(np.arange(0, 15, 0.5) * max_m, minor=[])
                ax.xaxis.set_ticks(xticks, minor=[])
                ax.set_ylim([self.rd_manhattan_range[0] * max_m, self.rd_manhattan_range[1] * max_m])
                n_bins = apos
                ax.set_xlim([0, n_bins])
                ax.grid()

            elif plot_type == "baf_mosaic":
                chroms = []
                snp_flag = (FLAG_USEMASK if self.snp_use_mask else 0) | (FLAG_USEID if self.snp_use_id else 0) | (
                    FLAG_USEHAP if self.snp_use_phase else 0)
                for c, (l, t) in self.reference_genome["chromosomes"].items():
                    snp_chr = io.snp_chromosome_name(c)
                    if len(self.chrom) == 0 or (snp_chr in self.chrom) or (c in self.chrom):
                        if io.signal_exists(snp_chr, bin_size, "SNP likelihood call", snp_flag) and \
                                io.signal_exists(snp_chr, bin_size, "SNP likelihood segments", snp_flag) and \
                                (Genome.is_autosome(c) or Genome.is_sex_chrom(c)):
                            chroms.append((snp_chr, l))

                apos = 0
                xticks = [0]

                cix = 0
                cmap = list(map(colors.to_rgba, plt.rcParams['axes.prop_cycle'].by_key()['color']))
                for c, l in chroms:
                    likelihood = io.get_signal(c, bin_size, "SNP likelihood call", snp_flag)
                    segments = segments_decode(io.get_signal(c, bin_size, "SNP likelihood segments", snp_flag))
                    call_pos = []
                    call_baf = []
                    call_c = []
                    for s, lh in zip(segments, likelihood):
                        b, p = likelihood_baf_pval(lh)
                        if b > 0 and len(s) > self.min_segment_size:
                            alpha = -np.log(p + 1e-40) / self.contrast
                            if alpha > 1:
                                alpha = 1
                            for pos in s:
                                call_pos.append(apos + pos)
                                call_baf.append(b)
                                color = cmap[cix % len(cmap)]
                                color = (color[0], color[1], color[2], alpha)
                                call_c.append(color)

                    ax.text(apos + l // bin_size // 2, 0.4, Genome.canonical_chrom_name(c),
                            fontsize=8, verticalalignment='bottom', horizontalalignment='center', )
                    plt.scatter(call_pos, call_baf, s=20, color=np.array(call_c), edgecolors='face', marker='|')
                    apos += l // bin_size
                    xticks.append(apos)
                    cix += 1

                ax.xaxis.set_ticklabels([])
                ax.yaxis.set_ticklabels([])
                ax.yaxis.set_ticks(np.arange(0, 0.5, 0.1), minor=[])
                ax.xaxis.set_ticks(xticks, minor=[])
                ax.set_ylim([0, 0.5])
                n_bins = apos
                ax.set_xlim([0, n_bins])
                ax.grid()

            elif plot_type == "rd_mean_shift":
                chroms = []
                flag = (FLAG_USEMASK if self.rd_use_mask else 0) | FLAG_GC_CORR

                for c, (l, t) in self.reference_genome["chromosomes"].items():
                    rd_chr = io.rd_chromosome_name(c)
                    if rd_chr is not None and len(self.chrom) == 0 or (rd_chr in self.chrom) or (c in self.chrom):
                        if (Genome.is_autosome(c) or Genome.is_sex_chrom(c)):
                            chroms.append((rd_chr, l))

                apos = 0
                xticks = [0]

                cix = 0
                cmap = list(map(colors.to_rgba, plt.rcParams['axes.prop_cycle'].by_key()['color']))
                for c, l in chroms:
                    call_pos = []
                    call_conc = []
                    call_c = []
                    if io.signal_exists(c, bin_size, "calls", flag):
                        calls = io.read_calls(c, bin_size, "calls", flag)

                        for call in calls:
                            if in_interval(call["size"], self.size_range) and in_interval(call["p_val"], self.p_range) \
                                    and in_interval(call["pN"], self.pN_range) \
                                    and in_interval(call["Q0"], self.Q0_range):
                                alpha = - np.log(call["p_val"] + 1e-40) / self.contrast
                                if alpha > 1:
                                    alpha = 1
                                if alpha < 0:
                                    alpha = 0
                                for pos in range(int(call["start"]) // bin_size, int(call["end"]) // bin_size + 1):
                                    call_pos.append(apos + pos)
                                    level = call["cnv"] * 2
                                    if level > 4:
                                        level = 4
                                    call_conc.append(level)
                                    if call["type"] == 1:
                                        call_c.append((0, 1, 0, alpha))
                                    elif call["type"] == -1:
                                        call_c.append((1, 0, 0, alpha))
                                    else:
                                        call_c.append((0, 0, 1, alpha))
                        ax.text(apos + l // bin_size // 2, 0.4, Genome.canonical_chrom_name(c),
                                fontsize=8, verticalalignment='bottom', horizontalalignment='center', )
                        plt.scatter(call_pos, call_conc, s=20, color=np.array(call_c), edgecolors='face', marker='|')
                        apos += l // bin_size
                        xticks.append(apos)
                        cix += 1

                ax.xaxis.set_ticklabels([])
                ax.yaxis.set_ticklabels([])
                ax.yaxis.set_ticks(np.arange(0, 4.0, 1.0), minor=[])
                ax.xaxis.set_ticks(xticks, minor=[])
                ax.set_ylim([0, 4.0])
                n_bins = apos
                ax.set_xlim([0, n_bins])
                ax.grid()

            elif plot_type == "combined_mosaic":
                chroms = []
                flag = (FLAG_USEMASK if self.snp_use_mask else 0) | (FLAG_USEID if self.snp_use_id else 0) | (
                    FLAG_USEHAP if self.snp_use_phase else 0) | (FLAG_USEMASK if self.rd_use_mask else 0) | FLAG_GC_CORR

                for c, (l, t) in self.reference_genome["chromosomes"].items():
                    snp_chr = io.snp_chromosome_name(c)
                    if snp_chr is not None and len(self.chrom) == 0 or (snp_chr in self.chrom) or (c in self.chrom):
                        if (Genome.is_autosome(c) or Genome.is_sex_chrom(c)):
                            chroms.append((snp_chr, l))

                apos = 0
                xticks = [0]

                cix = 0
                cmap = list(map(colors.to_rgba, plt.rcParams['axes.prop_cycle'].by_key()['color']))
                for c, l in chroms:
                    call_pos = []
                    call_conc = []
                    call_c = []
                    if io.signal_exists(c, bin_size, "calls combined", flag):
                        calls = io.read_calls(c, bin_size, "calls combined", flag)

                        for call in calls:
                            if call["bins"] > self.min_segment_size:
                                alpha = -np.log(call["p_val"] + 1e-40) / self.contrast
                                if alpha > 1:
                                    alpha = 1
                                for pos in range(int(call["start"]) // bin_size, int(call["end"]) // bin_size + 1):
                                    call_pos.append(apos + pos)
                                    call_conc.append(call["models"][0][4])
                                    if call["type"] == 1:
                                        call_c.append((0, 1, 0, alpha))
                                    elif call["type"] == -1:
                                        call_c.append((1, 0, 0, alpha))
                                    else:
                                        call_c.append((0, 0, 1, alpha))

                        ax.text(apos + l // bin_size // 2, 0.4, Genome.canonical_chrom_name(c),
                                fontsize=8, verticalalignment='bottom', horizontalalignment='center', )
                        plt.scatter(call_pos, call_conc, s=20, color=np.array(call_c), edgecolors='face', marker='|')
                        apos += l // bin_size
                        xticks.append(apos)
                        cix += 1

                ax.xaxis.set_ticklabels([])
                ax.yaxis.set_ticklabels([])
                ax.yaxis.set_ticks(np.arange(0, 1.0, 0.1), minor=[])
                ax.xaxis.set_ticks(xticks, minor=[])
                ax.set_ylim([0, 1.0])

                n_bins = apos
                ax.set_xlim([0, n_bins])
                ax.grid()

        self.fig_show(suffix="manhattan" if plot_type == "rd" else "snp_calls")

 