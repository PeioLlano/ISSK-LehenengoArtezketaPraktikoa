#!/bin/bash

eguna=$(date +%d-%m-%Y);
atzo=$(date -d yesterday +%d-%m-%Y);

$(rsync -av --compare-dest=/var/tmp/Backups/$atzo /home/peio/Segurtasuna /var/tmp/Backups/$gaur);
