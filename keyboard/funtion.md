motion

next charcter h , <right arrow> 
prev charcter l , <left arrow>

next line j <down arrow>
prev line k <up arrow>

next beginning of the word w
prev beginning of the word b

next end of the word e
prev end of the word ge

sentence backward (
sentence forward  )

next empty line/paragraph }
Prev empty line/paragraph {

Start of line 0
Start of line (non ws) ^
End of line $

First line of the file gg
Last line of the file G

search backward for the Nth occurrence of the ident under the cursor
search forward for the Nth occurrence of the ident under the cursor
find the next (curly/square) bracket on this line and go to its match, or go to matching comment bracket, or go to matching preprocessor directive.

{count}%             1  go to N percentage in the file
_                    1  cursor to the first CHAR N - 1 lines lower
|                    1  cursor to column N


f{char}              1  cursor to Nth occurrence of {char} to the right
F{char}              1  cursor to the Nth occurrence of {char} to the left
t{char}              1  cursor till before Nth occurrence of {char} to the right
T{char}              1  cursor till after Nth occurrence of {char} to the left

,                    1  repeat latest f, t, F or T in opposite direction N times
;                    1  repeat latest f, t, F or T N times

/<CR>                1  search forward for {pattern} of last search
/{pattern}<CR>       1  search forward for the Nth occurrence of {pattern}
?<CR>                1  search backward for {pattern} of last search
?{pattern}<CR>       1  search backward for the Nth previous occurrence of {pattern}

{ "%", desc = "Matching (){}[]" },

scrolling

scroll N screens Backwards
scroll N screens Forward

scroll N lines Upwards (default: half a screen)
scroll Down N lines (default: half a screen)

move window three lines up
move window three lines down
move window six columns left
move window six columns right
move window one page up
move window one page down
move window one page left
move window one page right
