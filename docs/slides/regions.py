
    def regions(self, ix, region):
        panels = self.panels
        bin_size = self.bin_size
        snp_flag = (FLAG_USEMASK if self.snp_use_mask else 0) | (FLAG_USEID if self.snp_use_id else 0) | (
            FLAG_USEHAP if self.snp_use_phase else 0)
        self.new_subgrid(len(panels), hspace=0.05, wspace=0.1)
        r = decode_region(region, max_size=1000000000)
        io = self.io[ix]
        for i in range(len(panels)):
            ax = self.next_subpanel(sharex=True)
            if i == 0 and self.title:
                ax.set_title(self.file_title(ix) + ": " + region.replace(",", ", "), position=(0.01, 0.93),
                             fontdict={'verticalalignment': 'bottom', 'horizontalalignment': 'left'},
                             color='C0')

            if panels[i] == "rd":
                g_p = [0]
                g_p_corr = [0]
                g_p_seg = [0]
                g_p_call = [0]
                g_p_call_mosaic = [0]
                g_p_call_mosaic_2d = [0]
                mean, stdev = 0, 0
                borders = []
                pos_x = []
                for c, (pos1, pos2) in r:
                    if pos2 == 1000000000:
                        pos2 = io.get_chromosome_length(c)
                        if pos2 is None:
                            pos2 = 1000000000
                    flag_rd = 0
                    if self.rd_use_mask:
                        flag_rd = FLAG_USEMASK
                    mean, stdev = io.rd_normal_level(bin_size, flag_rd | FLAG_GC_CORR)
                    his_p = io.get_signal(c, bin_size, "RD", flag_rd)
                    his_p_corr = io.get_signal(c, bin_size, "RD", flag_rd | FLAG_GC_CORR)
                    his_p_seg = io.get_signal(c, bin_size, "RD partition", flag_rd | FLAG_GC_CORR)
                    his_p_call = io.get_signal(c, bin_size, "RD call", flag_rd | FLAG_GC_CORR)
                    his_p_mosaic_seg = io.get_signal(c, bin_size, "RD mosaic segments",
                                                     flag_rd | FLAG_GC_CORR)
                    his_p_mosaic_seg = segments_decode(his_p_mosaic_seg)
                    his_p_mosaic_call = io.get_signal(c, bin_size, "RD mosaic call",
                                                      flag_rd | FLAG_GC_CORR)
                    if self.snp_use_phase:
                        his_p_mosaic_seg_2d = io.get_signal(c, bin_size, "RD mosaic segments 2d phased",
                                                            flag_rd | FLAG_GC_CORR)
                        his_p_mosaic_call_2d = io.get_signal(c, bin_size, "RD mosaic call 2d phased",
                                                             flag_rd | FLAG_GC_CORR)
                    else:
                        his_p_mosaic_seg_2d = io.get_signal(c, bin_size, "RD mosaic segments 2d",
                                                            flag_rd | FLAG_GC_CORR)
                        his_p_mosaic_call_2d = io.get_signal(c, bin_size, "RD mosaic call 2d",
                                                             flag_rd | FLAG_GC_CORR)
                    his_p_mosaic_seg_2d = segments_decode(his_p_mosaic_seg_2d)
                    his_p_mosaic = np.zeros_like(his_p) * np.nan
                    if his_p_mosaic_call is not None and len(his_p_mosaic_call) > 0 and ("rd_mosaic" in self.callers):
                        for seg, lev in zip(list(his_p_mosaic_seg), list(his_p_mosaic_call[0])):
                            for segi in seg:
                                his_p_mosaic[segi] = lev
                    his_p_mosaic_2d = np.zeros_like(his_p) * np.nan
                    if his_p_mosaic_call_2d is not None and len(his_p_mosaic_call_2d) > 0 and (
                            "combined_mosaic" in self.callers):
                        for seg, lev in zip(list(his_p_mosaic_seg_2d), list(his_p_mosaic_call_2d[0])):
                            for segi in seg:
                                his_p_mosaic_2d[segi] = lev
                    start_bin = (pos1 - 1) // bin_size
                    end_bin = pos2 // bin_size
                    bins = len(list(his_p[start_bin:end_bin]))
                    pos_x.extend(range(pos1, pos2 + bin_size, bin_size)[0:bins])

                    g_p.extend(list(his_p[start_bin:end_bin]))
                    g_p_corr.extend(list(his_p_corr[start_bin:end_bin]))
                    if his_p_seg is not None and len(his_p_seg) > 0 and self.rd_partition:
                        g_p_seg.extend(list(his_p_seg[start_bin:end_bin]))
                    if his_p_call is not None and len(his_p_call) > 0 and self.rd_call and (
                            "rd_mean_shift" in self.callers):
                        g_p_call.extend(list(his_p_call[start_bin:end_bin]))
                    if his_p_mosaic_call is not None and len(his_p_mosaic_call) > 0 and self.rd_call and (
                            "rd_mosaic" in self.callers):
                        g_p_call_mosaic.extend(list(his_p_mosaic[start_bin:end_bin]))
                    if his_p_mosaic_call_2d is not None and len(his_p_mosaic_call_2d) > 0 and self.rd_call and (
                            "combined_mosaic" in self.callers):
                        g_p_call_mosaic_2d.extend(list(his_p_mosaic_2d[start_bin:end_bin]))
                    borders.append(len(g_p) - 1)

                def format_func(value, tick_number):
                    ix = int(value)
                    if ix + 1 < len(pos_x):
                        p = pos_x[ix] + (pos_x[ix + 1] - pos_x[ix]) * (value - ix)
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    elif ix < len(pos_x):
                        p = pos_x[ix]
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    else:
                        return ""

                l = len(g_p)
                if i == len(panels) - 1:
                    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
                    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
                    ax.set_xlim([-l * 0.0, (l - 1) * 1.0])
                    ax.xaxis.grid()
                else:
                    plt.setp(ax.get_xticklabels(), visible=False)

                if (self.rd_range[1] - self.rd_range[0]) < 30:
                    ax.yaxis.set_ticks(np.arange(int(self.rd_range[0]), int(self.rd_range[1] + 1), 1) * mean / 2,
                                       minor=[])
                    ax.yaxis.set_ticklabels([str(i) for i in range(int(self.rd_range[0]), int(self.rd_range[1] + 1))])
                ax.set_ylim([self.rd_range[0] * mean / 2, self.rd_range[1] * mean / 2])
                ax.set_ylabel("Read depth")
                ax.yaxis.grid()

                if self.rd_raw:
                    ax.step(g_p, self.rd_colors[0], label="raw")
                if self.rd_corrected:
                    ax.step(g_p_corr, self.rd_colors[1], label="GC corrected")
                if len(g_p_seg) > 1:
                    plt.step(g_p_seg, self.rd_colors[2], label="partitioning")
                if len(g_p_call) > 1:
                    plt.step(g_p_call, self.rd_colors[3], label="cnv calls")
                if len(g_p_call_mosaic) > 1:
                    plt.step(g_p_call_mosaic, self.rd_colors[4], label="mosaic cnv calls")
                if len(g_p_call_mosaic_2d) > 1:
                    plt.step(g_p_call_mosaic_2d, self.rd_colors[5], label="combined cnv calls")
                for i in borders[:-1]:
                    ax.axvline(i, color="g", lw=1)
                if self.legend:
                    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
                self.fig.add_subplot(ax)

            elif panels[i] == "snp":
                borders = []
                hpos = []
                baf = []
                color = []
                alpha = 0.7
                start_pos = 0
                pos_x = []
                for c, (pos1, pos2) in r:
                    if pos2 == 1000000000:
                        pos2 = io.get_chromosome_length(c)
                        if pos2 is None:
                            pos2 = 1000000000
                    pos, ref, alt, nref, nalt, gt, flag, qual = io.read_snp(c)
                    ix = 0
                    mdp = 0
                    while ix < len(pos) and pos[ix] <= pos2:
                        if pos[ix] >= pos1 and (nref[ix] + nalt[ix]) != 0 and ((not self.snp_use_id) or (flag[ix] & 1)):
                            hpos.append((start_pos + pos[ix] - pos1) / bin_size)
                            if pos[ix] - pos1 > mdp:
                                mdp = pos[ix] - pos1
                            if gt[ix] != 5:
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
                    start_pos += pos2 - pos1
                    pos_x.extend(range(pos1, pos2 + bin_size, bin_size))
                    borders.append(start_pos / bin_size)

                def format_func(value, tick_number):
                    ix = int(value)
                    if ix + 1 < len(pos_x):
                        p = pos_x[ix] + (pos_x[ix + 1] - pos_x[ix]) * (value - ix)
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    elif ix < len(pos_x):
                        p = pos_x[ix]
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    else:
                        return ""

                l = len(pos_x)
                if i == len(panels) - 1:
                    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
                    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
                    ax.set_xlim([-l * 0.0, (l - 1) * 1.0])
                    ax.xaxis.grid()
                else:
                    plt.setp(ax.get_xticklabels(), visible=False)

                # ax.xaxis.set_ticklabels([])
                ax.yaxis.set_ticks([0, 0.25, 0.5, 0.75, 1.0], minor=[])
                ax.yaxis.set_ticklabels(["0", "1/4", "1/2", "3/4", "1"])
                ax.set_ylabel("Allele frequency")
                # l = max(hpos)
                ax.set_ylim([-0.05, 1.05])
                # ax.set_xlim([0, borders[-1]])
                ax.yaxis.grid()
                if self.markersize == "auto":
                    ax.scatter(hpos, baf, marker='.', edgecolor=color, c=color, s=10, alpha=alpha)
                else:
                    ax.scatter(hpos, baf, marker='.', edgecolor=color, c=color, s=self.markersize, alpha=alpha)

                for i in borders[:-1]:
                    ax.axvline(i, color="g", lw=1)
                self.fig.add_subplot(ax)

            elif panels[i] == "snv" or panels[i][:4] == "snv:":
                callset = "default"
                if panels[i][:4] == "snv:":
                    callset = panels[i].split(":")[1]
                borders = []
                hpos = []
                baf = []
                color = []
                alpha = 0.7
                start_pos = 0
                pos_x = []
                for c, (pos1, pos2) in r:
                    if pos2 == 1000000000:
                        pos2 = io.get_chromosome_length(c)
                        if pos2 is None:
                            pos2 = 1000000000
                    pos, ref, alt, nref, nalt, gt, flag, qual = io.read_snp(c, callset=callset)
                    ix = 0
                    mdp = 0
                    while ix < len(pos) and pos[ix] <= pos2:
                        if pos[ix] >= pos1 and (nref[ix] + nalt[ix]) != 0:
                            hpos.append((start_pos + pos[ix] - pos1) / bin_size)
                            if pos[ix] - pos1 > mdp:
                                mdp = pos[ix] - pos1
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
                    start_pos += pos2 - pos1
                    pos_x.extend(range(pos1, pos2 + bin_size, bin_size))
                    borders.append(start_pos / bin_size)

                def format_func(value, tick_number):
                    ix = int(value)
                    if ix + 1 < len(pos_x):
                        p = pos_x[ix] + (pos_x[ix + 1] - pos_x[ix]) * (value - ix)
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    elif ix < len(pos_x):
                        p = pos_x[ix]
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    else:
                        return ""

                l = len(pos_x)
                if i == len(panels) - 1:
                    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
                    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
                    ax.set_xlim([-l * 0.0, (l - 1) * 1.0])
                else:
                    plt.setp(ax.get_xticklabels(), visible=False)
                ax.xaxis.grid()
                ax.yaxis.set_ticklabels([])
                ax.yaxis.set_ticks([0, 0.25, 0.5, 0.75, 1.0], minor=[])
                ax.yaxis.set_ticklabels(["0", "1/4", "1/2", "3/4", "1"])
                ax.set_ylabel("Allele frequency")
                ax.set_ylim([0., 1.])
                ax.yaxis.grid()
                if self.markersize == "auto":
                    ax.scatter(hpos, baf, marker='.', edgecolor=color, c=color, s=10, alpha=alpha)
                else:
                    ax.scatter(hpos, baf, marker='.', edgecolor=color, c=color, s=self.markersize, alpha=alpha)

                for i in borders[:-1]:
                    ax.axvline(i, color="g", lw=1)
                self.fig.add_subplot(ax)

            elif panels[i] == "baf":
                g_baf, g_maf, g_i1, g_i2 = [0], [0], [0], [0]
                borders = []
                pos_x = []

                for c, (pos1, pos2) in r:
                    if pos2 == 1000000000:
                        pos2 = io.get_chromosome_length(c)
                        if pos2 is None:
                            pos2 = 1000000000

                    flag_snp = (FLAG_USEMASK if self.snp_use_mask else 0) | (FLAG_USEID if self.snp_use_id else 0) | (
                        FLAG_USEHAP if self.snp_use_phase else 0)
                    baf = io.get_signal(c, bin_size, "SNP baf", flag_snp)
                    maf = io.get_signal(c, bin_size, "SNP maf", flag_snp)
                    i1 = io.get_signal(c, bin_size, "SNP i1", flag_snp)
                    i2 = io.get_signal(c, bin_size, "SNP i2", flag_snp)

                    start_bin = (pos1 - 1) // bin_size
                    end_bin = pos2 // bin_size
                    bins = len(list(baf[start_bin:end_bin]))
                    pos_x.extend(range(pos1, pos2 + bin_size, bin_size)[0:bins])

                    g_baf.extend(list(baf[start_bin:end_bin]))
                    g_maf.extend(list(maf[start_bin:end_bin]))
                    g_i1.extend(list(i1[start_bin:end_bin]))
                    g_i2.extend(list(i2[start_bin:end_bin]))
                    borders.append(len(g_baf) - 1)

                def format_func(value, tick_number):
                    ix = int(value)
                    if ix + 1 < len(pos_x):
                        p = pos_x[ix] + (pos_x[ix + 1] - pos_x[ix]) * (value - ix)
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    elif ix < len(pos_x):
                        p = pos_x[ix]
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    else:
                        return ""

                l = len(g_baf)
                if i == len(panels) - 1:
                    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
                    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
                    ax.set_xlim([-l * 0.0, (l - 1) * 1.0])
                    ax.xaxis.grid()

                ax.yaxis.set_ticklabels([])
                ax.yaxis.set_ticks([0, 0.25, 0.5, 0.75, 1.0], minor=[])
                ax.yaxis.set_ticklabels(["0", "1/4", "1/2", "3/4", "1"])
                ax.set_ylabel("Allele frequency")

                ax.set_ylim(self.baf_range)
                # ax.set_xlim([-l * 0.0, l * 1.0])

                ax.yaxis.grid()
                # ax.xaxis.grid()
                if self.plot_baf:
                    ax.step(g_baf, self.baf_colors[0], label="BAF")
                if self.plot_maf:
                    ax.step(g_maf, self.baf_colors[1], label="MAF")
                if self.plot_dbaf:
                    ax.step(g_i1, self.baf_colors[2], label="I1")
                if self.legend:
                    ax.legend()
                for i in borders[:-1]:
                    ax.axvline(i, color="g", lw=1)
                self.fig.add_subplot(ax)

            elif panels[i] == "likelihood":
                borders = []
                gl = []
                call_pos = []
                call_i1 = []
                call_i2 = []
                call_c = []
                call_pos_2d = []
                call_i1_2d = []
                call_i2_2d = []
                call_c_2d = []
                tlen = 0
                tlen_2d = 0
                pos_x = []
                for c, (pos1, pos2) in r:
                    if pos2 == 1000000000:
                        pos2 = io.get_chromosome_length(c)
                        if pos2 is None:
                            pos2 = 1000000000
                    likelihood = io.get_signal(c, bin_size, "SNP likelihood", snp_flag)
                    start_bin = (pos1 - 1) // bin_size
                    end_bin = pos2 // bin_size
                    bins = len(list(likelihood[start_bin:end_bin]))
                    pos_x.extend(range(pos1, pos2 + bin_size, bin_size)[0:bins])
                    gl.extend(list(likelihood[start_bin:end_bin]))
                    borders.append(len(gl) - 1)
                    if self.snp_call and ("baf_mosaic" in self.callers):
                        likelihood_call = io.get_signal(c, bin_size, "SNP likelihood call", snp_flag)
                        segments = segments_decode(io.get_signal(c, bin_size, "SNP likelihood segments", snp_flag))

                        for s, lh in zip(segments, likelihood_call):
                            i1, i2, p = likelihood_pixels_pval(lh)
                            if i1 != i2 and len(s) > self.min_segment_size:
                                alpha = -np.log(p + 1e-40) / self.contrast
                                if alpha > 1:
                                    alpha = 1
                                for pos in s:
                                    if pos >= start_bin and pos < end_bin:
                                        call_pos.append(pos - start_bin + tlen)
                                        call_i1.append(min(i1, i2))
                                        call_i2.append(max(i1, i2))
                                        color = colors.to_rgb(self.lh_colors[0]) + (alpha,)
                                        call_c.append(color)
                        tlen += end_bin - start_bin
                    if self.snp_call and ("combined_mosaic" in self.callers):
                        likelihood_call = io.get_signal(c, bin_size, "SNP likelihood call 2d", snp_flag)
                        segments = segments_decode(io.get_signal(c, bin_size, "SNP likelihood segments 2d", snp_flag))

                        for s, lh in zip(segments, likelihood_call):
                            i1, i2, p = likelihood_pixels_pval(lh)
                            if i1 != i2 and len(s) > self.min_segment_size:
                                alpha = -np.log(p + 1e-40) / self.contrast
                                if alpha > 1:
                                    alpha = 1
                                for pos in s:
                                    if pos >= start_bin and pos < end_bin:
                                        call_pos_2d.append(pos - start_bin + tlen_2d)
                                        call_i1_2d.append(min(i1, i2))
                                        call_i2_2d.append(max(i1, i2))
                                        color = colors.to_rgb(self.lh_colors[1]) + (alpha,)
                                        call_c_2d.append(color)
                        tlen_2d += end_bin - start_bin

                def format_func(value, tick_number):
                    ix = int(value)
                    if ix + 1 < len(pos_x):
                        p = pos_x[ix] + (pos_x[ix + 1] - pos_x[ix]) * (value - ix)
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    elif ix < len(pos_x):
                        p = pos_x[ix]
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    else:
                        return ""

                img = np.array(gl).transpose()
                l = img.shape[1]
                if i == len(panels) - 1:
                    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
                    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
                    ax.set_xlim([-l * 0.0, (l - 1) * 1.0])
                    # ax.xaxis.grid()
                else:
                    plt.setp(ax.get_xticklabels(), visible=False)

                ax.imshow(img, aspect='auto', extent=[0, l, 0, img.shape[0] - 1])
                # ax.xaxis.set_ticklabels([])
                ax.yaxis.set_ticks([0, img.shape[0] / 4, img.shape[0] / 2, 3 * img.shape[0] / 4, img.shape[0] - 1],
                                   minor=[])
                ax.yaxis.set_ticklabels(["1", "3/4", "1/2", "1/4", "0"])
                ax.set_ylabel("Allele frequency")
                # ax.xaxis.set_ticks(np.arange(0, len(gl), 50), minor=[])
                # ax.set_xlim([-0.5, img.shape[1] - 0.5])
                ax.set_ylim([self.baf_range[0] * img.shape[0], self.baf_range[1] * img.shape[0]])
                if self.snp_call and ("baf_mosaic" in self.callers):
                    plt.scatter(call_pos, call_i1, s=self.lh_markersize, color=np.array(call_c), edgecolors='face',
                                marker=self.lh_marker)
                    plt.scatter(call_pos, call_i2, s=self.lh_markersize, color=np.array(call_c), edgecolors='face',
                                marker=self.lh_marker)
                if self.snp_call and ("combined_mosaic" in self.callers):
                    plt.scatter(call_pos_2d, call_i1_2d, s=self.lh_markersize, color=np.array(call_c_2d),
                                edgecolors='face', marker=self.lh_marker)
                    plt.scatter(call_pos_2d, call_i2_2d, s=self.lh_markersize, color=np.array(call_c_2d),
                                edgecolors='face', marker=self.lh_marker)

                for i in borders[:-1]:
                    ax.axvline(i + 1, color="g", lw=1)
                self.fig.add_subplot(ax)

            elif panels[i] == "CN":
                borders = []
                gh1 = []
                gh2 = []
                tlen = 0
                tlen_2d = 0
                for c, (pos1, pos2) in r:
                    if pos2 == 1000000000:
                        pos2 = io.get_chromosome_length(c)
                        if pos2 is None:
                            pos2 = 1000000000

                    his_p = io.get_signal(c, bin_size, "RD p", flag_rd)
                    start_bin = (pos1 - 1) // bin_size
                    end_bin = pos2 // bin_size
                    if end_bin > len(his_p):
                        end_bin = len(his_p)
                    h1 = np.array([0] * (end_bin - start_bin))
                    h2 = np.array([0] * (end_bin - start_bin))
                    h1[his_p[start_bin:end_bin] != 0] = 1
                    h2[his_p[start_bin:end_bin] != 0] = 1

                    flag = (FLAG_USEMASK if self.snp_use_mask else 0) | (FLAG_USEID if self.snp_use_id else 0) | (
                        FLAG_USEHAP if self.snp_use_phase else 0) | (
                               FLAG_USEMASK if self.rd_use_mask else 0) | FLAG_GC_CORR
                    flag_rd = FLAG_GC_CORR | (FLAG_USEMASK if self.rd_use_mask else 0)
                    if io.signal_exists(c, bin_size, "calls combined", flag):
                        calls = io.read_calls(c, bin_size, "calls combined", flag)
                        segments = io.get_signal(c, bin_size, "RD mosaic segments 2d phased", FLAG_GC_CORR)
                        print(segments)
                        segments = segments_decode(segments)

                        for call in calls:
                            for b in segments[int(call["segment"])]:
                                if b < end_bin and b >= start_bin:
                                    h1[b - start_bin] = call["models"][0][1]
                                    h2[b - start_bin] = call["models"][0][2]
                    gh1.extend(list(h1))
                    gh2.extend(list(h2))
                    borders.append(len(gh1) - 1)
                x = range(len(gh1))
                plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
                plt.stackplot(x, gh1, gh2, baseline='sym')

                def format_func(value, tick_number):
                    ix = int(value)
                    if ix + 1 < len(pos_x):
                        p = pos_x[ix] + (pos_x[ix + 1] - pos_x[ix]) * (value - ix)
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    elif ix < len(pos_x):
                        p = pos_x[ix]
                        return "{0} Mbp".format(int(p / 100) / 10000)
                    else:
                        return ""

                l = len(gh1)
                if i == len(panels) - 1:
                    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
                    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
                    ax.set_xlim([-l * 0.0, (l - 1) * 1.0])
                    ax.xaxis.grid()

                for i in borders[:-1]:
                    ax.axvline(i + 0.5, color="g", lw=1)
                self.fig.add_subplot(ax)

 