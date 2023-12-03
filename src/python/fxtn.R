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
load.libraries(c('rio','psych','ggplot2','afex','plyr','dplyr','lsmeans','knitr'),libpath)

# for pdf plots
pdf.options(family="NimbusSan", useDingbats=FALSE)

df <- read.csv('fxtn.csv')
# if we need to remove a particular subset
#df <- filter(df, block == "test")

# filter out participants who apparantly did not pay attention to the task
#df <- filter(df, subj != "s01" & subj != "s02" & subj != "s04")

#subj,marker,ojbect,timestamp,x,y,duration,sacc_amplitude,sacc_dur
df$subj <- factor(df$subj)
df$task <- factor(df$task)

describe(df$duration)
describe(df$sacc_amplitude)

# selection of data points based on fixation duration and saccade amplitude
#df <- df[which(.08 < df$duration & df$duration < 1), ]
df <- df[which(df$sacc_amplitude > 0.00001), ]

#..Saccade amplitude..........................................................#

(fit <- aov_ez(data = df,
               id = "subj",
               dv = "sacc_amplitude",
               between = c('task'),
               type = 3,
               factorize = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

(t <- lsmeans(fit, c('task'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

samp.plot <- ggplot(tab,
                    aes(x = task, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Mean saccade amplitude (deg.)") +
                    xlab('Task') +
                    theme(legend.position = "none")

plotName = "./figs/samp.pdf"
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


#..Fixation duration..........................................................#
(fit <- aov_ez(data = df,
               id = "subj",
               dv = "duration",
               between = c('task'),
               type = 3,
               factorize = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

describe(df$duration)

(t <- lsmeans(fit, c('task'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

fdur.plot <- ggplot(tab,
                    aes(x = task, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Mean fixation duration (sec.)") +
                    xlab('Task') +
                    theme(legend.position = "none")

plotName = "./figs/dur.pdf"
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

#..Time per task (detection only)..........................................................#
dfOld <- df
df <- filter(df, detectionstatus=="True")
(fit <- aov_ez(data = df,
               id = "subj",
               dv = "time",
               between = c('task'),
               type = 3,
               factorize = FALSE))
summary(fit)

# nicer table
kable(nice(fit,es="ges"))

describe(df$duration)

(t <- lsmeans(fit, c('task'), contr = 'pairwise'))
tab <- summary(t$lsmeans)

fdur.plot <- ggplot(tab,
                    aes(x = task, y = lsmean)) +
                    geom_bar(position=position_dodge(), stat="identity",
                          colour="#303030",fill="#d94801",alpha=.7) +
#                         colour="#303030",fill="#045a8d",alpha=.7) +
#                   scale_fill_brewer(palette="Blues") +
                    scale_fill_brewer(palette="Oranges") +
                    geom_errorbar(aes(ymin=lsmean-SE, ymax=lsmean+SE),
                                  width=.2, size=.3,
                                  position=position_dodge(.9)) +
		    theme_bw(base_size=18) + 
                    ylab("Mean task duration (sec.)") +
                    xlab('Task') +
                    theme(legend.position = "none")

plotName = "./figs/task_time.pdf"
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

df <- dfOld