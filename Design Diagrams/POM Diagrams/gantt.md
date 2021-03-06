```mermaid
gantt

title Project Plan

dateFormat DD-MM-YY
axisFormat %U

section Project Prerequisites
Project Description     :pd, 05-01-22, 15d

section Research
Information Gathering   :inf1, 22-01-22, 60d
Write Interviews        :i1, 04-02-22, 5d
Perform Interviews       :i2, 09-02-22, 1d
Transcribe Interviews   :i3, after i2, 7d
Interview Analysis      :after i3, 14d

section Requirements
Requirements            :r1, 08-03-22, 10d
Requirements Analysis   :r2, after r1, 3d

section Design
System Design           :d1, 24-03-22, 7d

section Sprint 1
Sprint 1 Refinement     :ref1, 01-04-22, 7d
Sprint 1 Development    :dev1, after ref1, 7d
Sprint 1 Retrospective  :retro1, after dev1, 1d

section Sprint 2
Sprint 2 Refinement     :ref2, after retro1, 7d
Sprint 2 Development    :dev2, after ref2, 7d
Sprint 2 Retrospective  :retro2, after dev2, 1d

section Sprint 3
Sprint 3 Refinement     :ref3, after retro2, 7d
Sprint 3 Development    :dev3, after ref3, 7d
Sprint 3 Retrospective  :retro3, after dev3, 1d

section Test System
System Tests            :test1, after retro3, 7d
User Tests              :test2, after retro3, 7d

section Report
Write Report            :active, write, 01-02-22, 28-05-22
Proof Read Report       :crit, after write, 4d
Handin Report           :milestone, report, 01-06-22, 1d
```