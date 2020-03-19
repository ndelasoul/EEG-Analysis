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

def combine(annot):
    raw.set_annotations(annot)
    reconstruct(raw)
    return 

def reconstruct(raw):
    events, event_ids = mne.events_from_annotations(raw)
    results(events)
    return
    

def results(events):
    in_num = input("Which event: ")
    e_stim = mne.pick_events(events, include=int(in_num))
    print(e_stim.shape)
    return

def load(in_vhdr, in_vmrk):
    raw = mne.io.read_raw_brainvision(in_vhdr, preload=True)
    annot = mne.read_annotations(in_vmrk)
    combine(annot)
    return 


if __name__ == '__main__':
    cwd_files = glob(os.path.join(os.getcwd(),'*'))
    pprint.pprint(cwd_files)
    in_vhdr = input("vhdr file: ")
    fdir = os.path.join(os.getcwd(),in_vhdr)
    in_vmrk = input("vmrk file: ")
    edir = os.path.join(os.getcwd(),in_vmrk)
    load(in_vhdr, in_vmrk)
