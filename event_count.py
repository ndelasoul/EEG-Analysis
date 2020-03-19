#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:55:58 2020

@author: nick
"""
from glob import glob
import os
import mne
import pprint

def load(in_vhdr):
    raw = mne.io.read_raw_brainvision(in_vhdr, preload=True)
    return raw

def annotate(in_vmrk, raw):
    annot = mne.read_annotations(in_vmrk)
    annot.save('annotations.txt')
    return annot, raw


def combine(annot, raw):
    raw.set_annotations(annot)
    return annot, raw

def reconstruct(raw):
    events, event_ids = mne.events_from_annotations(raw)
    print(event_ids)
    return
    
"""
def results(events, in_num):
    e_stim = mne.pick_events(events, include=in_num)
    print(e_stim.shape)
    return
"""

if __name__ == '__main__':
    cwd_files = glob(os.path.join(os.getcwd(),'*'))
    pprint.pprint(cwd_files)
    in_vhdr = input("vhdr file: ")
    fdir = os.path.join(os.getcwd(),in_vhdr)
    load(fdir)

    in_vmrk = input("vmrk file: ")
    edir = os.path.join(os.getcwd(),in_vmrk)
    annotate(edir)
"""
    in_num = input("Which event:")
    ndir = os.path.join(os.getcwd(),in_num)
    results(in_num)
"""
    
