#!/bin/zsh

#To make streaming app read m3u file you are creating you have to include this at the beginning of it
echo "#EXTM3U" > ./scraped-m3us/k.m3u

#Remove (almost) empty .m3u files (<5 bytes)
fd -S -5b '.*m3u' ./scraped-m3us

#Find only stuff I'm looking for (change by your preferences!)
rg -NI -A 1 "SVT|FR:|SW:|Animal|EX.*Y.*U|CRO:|Visat|Pluto|FOX.*(HD|Crime|Life|Movies)|Discovery.*(Channel|Sci)|Nat.*Geo" >> ./scraped-m3us/k.m3u

#Remove uneccesary  -- lines inside k.m3u
perl -p -i -e "s/\-//g" ./scraped-m3us/k.m3u


