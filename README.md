# Testing Inputs Into An Emulator
[![Stability](https://img.shields.io/badge/Status-stable-COLO.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Version](https://img.shields.io/badge/ver-0.1.0-TEAL.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)  
Authored: Jeffrey Ng  

## Emulator Environment(s): 
### Visual Boy Advance
[Download emulator](http://www.emulator-zone.com/doc.php/gba/vboyadvance.html)

#### Game Boy Advanced
##### Windowing
|Dimensions |Position 
|:---       |:---
|900x665px  |Top left most corner
Note: We are utilising VBA's built-in x3 video scalar. Results will vary on your machine  
##### Joypad Configuration
|Button     |Key
|:---       |:---
|Up         |W
|Down       |S
|Left       |A
|Right      |D
|A Button   |Z
|B Button   |X
|L Button   |Unbounded
|R Button   |Unbounded
|Select     |BACKSPACE
|Start      |ENTER
|Speed      |SPACE
|Capture    |F12
|GS         |C

#### DS
##### Windowing
|Dimensions |Position 
|:---       |:---

##### Joypad Configuration
|Button     |Key
|:---       |:---

## Necessary libraries
### Player driver
- NumPy:  
`pip install numpy`
- PIL:  
`pip install Pillow`
- CV2:  
`pip install cv2`

### Key logger
- Pynput:  
`pip install pynput`

