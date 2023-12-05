ver_mjr = R.Version()$major
ver_mnr = unlist(strsplit(R.Version()$minor,"\\."))[1]
lpath = sprintf("~/AppData/Local/R/win-library/%s.%s",ver_mjr,ver_mnr)
rversion = R.Version()
platform = Sys.info()['sysname']
print(sprintf("R version %s.%s running on %s",ver_mjr,ver_mnr,platform))
if(platform == "Windows") {
   if(!file.exists(lpath)) {
     dir.create(lpath,recursive=TRUE)
   }
   libpath <- c(lpath)
} else{
  libpath <- .libPaths()
}

source('custom.R')

# load plyr before dplyr
load.libraries(c('tidyverse','rio','psych','ggplot2','afex','lsmeans','knitr'),libpath)

# for pdf plots
pdf.options(family="NimbusSan", useDingbats=FALSE)

raw.aoi <- read.csv('fxtn-aois.csv')

# Detection Status and percentFixated (only stimuli that had a change) #############################################
df = raw.aoi %>%
    group_by(subj, detectionstatus) %>%
    filter(stim != "set_4") %>%
    summarise(changeFixated = length(which(aoi_order == 1)),
                changeNotFixated = length(which(aoi_order != 1))) %>%
    mutate(percentFixated = changeFixated / (changeFixated + changeNotFixated))

(fit <- aov_ez(data = df,
               id = "subj",
               dv = "percentFixated",
               between = c('detectionstatus'),
               type = 3,
               factorize = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

#describe(df$duration)

(t <- lsmeans(fit, c('detectionstatus'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

fdur.plot <- ggplot(tab,
                    aes(x = detectionstatus, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Changed AOI Fixation Percentage (%)") +
                    xlab('Change Detected') +
                    theme(legend.position = "none")

plotName = "./figs/fixationPercentage-detection.pdf"
pdf(plotName, encoding="ISOLatin2")
print(fdur.plot)
dev.off()
embedFonts(plotName, "pdfwrite", outfile = plotName,
        fontpaths =
          c("/sw/share/texmf-dist/fonts/type1/urw/",
            "/usr/share/texmf/fonts/type1/urw/",
            "/usr/local/teTeX/share/texmf-dist/fonts/type1/urw/",
            "/opt/local/share/texmf-texlive/fonts/type1/",
            "/usr/share/texmf-texlive/fonts/type1/urw/",
            "/usr/local/texlive/texmf-local/fonts/type1/urw/"))

# Last 20 Fixations #############################################
df = raw.aoi %>%
    filter(stim != "set_4") %>%
    group_by(subj, stim) %>%
    slice(tail(row_number(), 20)) %>%
    ungroup() %>%
    group_by(subj, detectionstatus) %>%
    summarise(changeFixated = length(which(aoi_order == 1)),
                changeNotFixated = length(which(aoi_order != 1))) %>%
    mutate(percentFixated = changeFixated / (changeFixated + changeNotFixated))

(fit <- aov_ez(data = df,
               id = "subj",
               dv = "percentFixated",
               between = c('detectionstatus'),
               type = 3,
               factorize = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

#describe(df$duration)

(t <- lsmeans(fit, c('detectionstatus'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

fdur.plot <- ggplot(tab,
                    aes(x = detectionstatus, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Changed AOI Fixation Percentage (%)") +
                    xlab('Change Detected') +
                    theme(legend.position = "none") + 
  scale_y_continuous(limits = c(0, NA), oob = scales::squish)

plotName = "./figs/last20-fixation-detection.pdf"
pdf(plotName, encoding="ISOLatin2")
print(fdur.plot)
dev.off()
embedFonts(plotName, "pdfwrite", outfile = plotName,
        fontpaths =
          c("/sw/share/texmf-dist/fonts/type1/urw/",
            "/usr/share/texmf/fonts/type1/urw/",
            "/usr/local/teTeX/share/texmf-dist/fonts/type1/urw/",
            "/opt/local/share/texmf-texlive/fonts/type1/",
            "/usr/share/texmf-texlive/fonts/type1/urw/",
            "/usr/local/texlive/texmf-local/fonts/type1/urw/"))

# Last 10 Fixations #############################################
df = raw.aoi %>%
    filter(stim != "set_4") %>%
    group_by(subj, stim) %>%
    slice(tail(row_number(), 10)) %>%
    ungroup() %>%
    group_by(subj, detectionstatus) %>%
    summarise(changeFixated = length(which(aoi_order == 1)),
                changeNotFixated = length(which(aoi_order != 1))) %>%
    mutate(percentFixated = changeFixated / (changeFixated + changeNotFixated))

(fit <- aov_ez(data = df,
               id = "subj",
               dv = "percentFixated",
               between = c('detectionstatus'),
               type = 3,
               factorize = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

#describe(df$duration)

(t <- lsmeans(fit, c('detectionstatus'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

fdur.plot <- ggplot(tab,
                    aes(x = detectionstatus, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Changed AOI Fixation Percentage") +
                    xlab('Change Detected') +
                    theme(legend.position = "none") + 
  scale_y_continuous(limits = c(0, NA), oob = scales::squish)

plotName = "./figs/last10-fixation-detection.pdf"
pdf(plotName, encoding="ISOLatin2")
print(fdur.plot)
dev.off()
embedFonts(plotName, "pdfwrite", outfile = plotName,
        fontpaths =
          c("/sw/share/texmf-dist/fonts/type1/urw/",
            "/usr/share/texmf/fonts/type1/urw/",
            "/usr/local/teTeX/share/texmf-dist/fonts/type1/urw/",
            "/opt/local/share/texmf-texlive/fonts/type1/",
            "/usr/share/texmf-texlive/fonts/type1/urw/",
            "/usr/local/texlive/texmf-local/fonts/type1/urw/"))

# Fixation Duration by image set
df = raw.aoi

(fit <- aov_ez(data = df,
               id = "subj",
               dv = "duration",
               between = c('stim'),
               type = 3,
               factorize = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

#describe(df$duration)

(t <- lsmeans(fit, c('stim'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

fdur.plot <- ggplot(tab,
                    aes(x = stim, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Mean fixation duration (ms.)") +
                    xlab('Stimulus') +
                    theme(legend.position = "none")

plotName = "./figs/stim-duration.pdf"
pdf(plotName, encoding="ISOLatin2")
print(fdur.plot)
dev.off()
embedFonts(plotName, "pdfwrite", outfile = plotName,
        fontpaths =
          c("/sw/share/texmf-dist/fonts/type1/urw/",
            "/usr/share/texmf/fonts/type1/urw/",
            "/usr/local/teTeX/share/texmf-dist/fonts/type1/urw/",
            "/opt/local/share/texmf-texlive/fonts/type1/",
            "/usr/share/texmf-texlive/fonts/type1/urw/",
            "/usr/local/texlive/texmf-local/fonts/type1/urw/"))

# Changed AOI Fixation Duration by image set
df = raw.aoi %>%
    filter(aoi_order == 1)

(fit <- aov_ez(data = df,
               id = "subj",
               dv = "duration",
               between = c('stim'),
               type = 3,
               factorize = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

#describe(df$duration)

(t <- lsmeans(fit, c('stim'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

fdur.plot <- ggplot(tab,
                    aes(x = stim, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Changed AOI Mean Fixation Duration (ms.)") +
                    xlab('Stimulus') +
                    theme(legend.position = "none")

plotName = "./figs/changedAOI-stim-duration.pdf"
pdf(plotName, encoding="ISOLatin2")
print(fdur.plot)
dev.off()
embedFonts(plotName, "pdfwrite", outfile = plotName,
        fontpaths =
          c("/sw/share/texmf-dist/fonts/type1/urw/",
            "/usr/share/texmf/fonts/type1/urw/",
            "/usr/local/teTeX/share/texmf-dist/fonts/type1/urw/",
            "/opt/local/share/texmf-texlive/fonts/type1/",
            "/usr/share/texmf-texlive/fonts/type1/urw/",
            "/usr/local/texlive/texmf-local/fonts/type1/urw/"))

### Fixation Duration Across AOIs
df = raw.aoi

(fit <- aov_ez(data = df,
               id = "subj",
               dv = "duration",
               within = c('aoi_order'),
               type = 3,
               factorize = FALSE, na.rm = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

(t <- lsmeans(fit, c('aoi_order'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

samp.plot <- ggplot(tab,
                    aes(x = aoi_order, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Mean fixation duration (ms.)") +
                    xlab('AOI') +
                    theme(legend.position = "none")

plotName = "./figs/AOI-duration.pdf"
pdf(plotName, encoding="ISOLatin2")
print(samp.plot)
dev.off()

embedFonts(plotName, "pdfwrite", outfile = plotName,
        fontpaths =
          c("/sw/share/texmf-dist/fonts/type1/urw/",
            "/usr/share/texmf/fonts/type1/urw/",
            "/usr/local/teTeX/share/texmf-dist/fonts/type1/urw/",
            "/opt/local/share/texmf-texlive/fonts/type1/",
            "/usr/share/texmf-texlive/fonts/type1/urw/",
            "/usr/local/texlive/texmf-local/fonts/type1/urw/"))