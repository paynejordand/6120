ver_mjr = R.Version()$major
ver_mnr = unlist(strsplit(R.Version()$minor,"\\."))[1]
lpath = sprintf("~/AppData/Local/R/win-library/%s.%s",ver_mjr,ver_mnr)
platform = Sys.info()['sysname']
print(sprintf("R version %s.%s running on %s",ver_mjr,ver_mnr,platform))
if(platform == "Windows") {
   if(!file.exists(lpath)) {
     dir.create(lpath,recursive=TRUE)
   }
   libpath <- c(lpath)
  .libPaths(libpath)
} else{
  libpath <- .libPaths()
}

source('custom.R')

#load.libraries(c('emmeans','sciplot','ez','psych','reshape','plyr','ggplot2','afex','dplyr','pastecs'),libpath)
load.libraries(c('tidyverse','emmeans','sciplot','psych','reshape','ggplot2','afex','pastecs'),libpath)

pdf.options(family="NimbusSan", useDingbats=FALSE)

source("tmcustom.R") 
source("lrheatmap.R") 
source("TMSP.R") 

args <- commandArgs(trailingOnly = TRUE)
#print(args)

naois <- as.integer(args[1])
print(sprintf("naois = %d\n",naois))

df <- read.csv("fxtn-aois.csv")

# ------------------------------------------------------------------------
# main analyses

M <- zeroTM(naois)
M

# school 0 or 1 is the school condition
#ddf <- df[which(df$school == "0"), ] # select condition
ddf <- df
#ddf
M_0 <- TransMatrix(M,data=ddf,
                    AOInamesVar="aoi_order",
                    SubjectsVar="subj",
                    FixOrderVar="order")
M_0 <- M
M_0

en_0 <- TransEntropy(M,data=ddf,
                    AOInamesVar="aoi_order",
                    SubjectsVar="subj",
                    FixOrderVar="order")
en_0 <- TMentrop
sen_0 <- StationaryEntropy(M,data=ddf,
                    AOInamesVar="aoi_order",
                    SubjectsVar="subj",
                    FixOrderVar="order")
sen_0 <- STentrop
TransPlot2(transMatrix=M_0,
           plotName="./figs/TM.pdf",
           plotColors=brewer.pal(9,"Oranges"),
           xLabels=c("1","2","3","4","5"),
           yLabels=c("1","2","3","4","5"),
           title="Grid",
           margin=c(6,6),
           annCex=1.3,
           cexR=1.4,
           cexC=1.4,
           cexAxis=1.6,
           annColor='black')
#          plotColors=brewer.pal(4,"Greys"),
#          annColor='#252525')

M <- zeroTM(naois)
M

##########################################################################
