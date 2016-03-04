#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
mimetype <- args[1]

train <- as.matrix(read.table(paste(mimetype,'_train.txt',sep=""), header=FALSE, sep = "\t"))
save(train,file='train.hist')

val <- as.matrix(read.table(paste(mimetype,'_val.txt',sep=""), header=FALSE, sep = "\t"))
save(val,file='val.hist')

test <- as.matrix(read.table(paste(mimetype,'_test.txt',sep=""), header=FALSE, sep = "\t"))
save(test,file='test.hist')

print("Completed splitting files...")

source('main2.R')
main2(gsub("-","/",mimetype))
