motions

  k
h   l
  j

h -> move to prev char
l -> move to next char
k -> move to prev line
j -> move to next line

  (
b   w
  )

{ "w", desc = "Next word" },
{ "b", desc = "Prev word" },
( -> move to prev sentence/statement
) -> move to next sentence/statement

  {
B   W
  }

{ "W", desc = "Next WORD" },
{ "B", desc = "Prev WORD" },
{ "{", desc = "Prev empty line" },
{ "}", desc = "Next empty line" },

e  desc = "Next end of word"
ge desc = "Prev end of word"

E  desc = "Next end of WORD"
gE -> move to prev big word at the ending

0 desc = "Start of line"
^ desc = "Start of line (non ws)"
$ desc = "End of line"

{ "gg", desc = "First line" },
{ "G", desc = "Last line" },

{ "f", desc = "Move to next char" },
{ "F", desc = "Move to prev char" },

{ "t", desc = "Move before next char" },
{ "T", desc = "Move before prev char" },


{ ",", desc = "Prev ftFT" },
{ ";", desc = "Next ftFT" },

{ "?", desc = "Search backward" },
{ "/", desc = "Search forward" },

{ "%", desc = "Matching (){}[]" },

 " ' ( ) { } `[` `]` < > b p s t w ```  B W  

text_objects 
{ "a", group = "around" },
    { 'a"', desc = '" string' },
    { "a'", desc = "' string" },
    { "a`` ` ``, desc = `` ` `` string" },
    { "ab", desc = "`()` block" },
    { "ap", desc = "paragraph" },
    { "as", desc = "sentence" },
    { "at", desc = "tag block" },
    { "aw", desc = "word with ws" },
    { "aB", desc = "`{}` block" },
    { "aW", desc = "WORD with ws" },
    { "a(", desc = "`()` block" },
    { "a)", desc = "`()` block" },
    { "a{", desc = "`{}` block" },
    { "a}", desc = "`{}` block" },
    { "a`[`", desc = "`[]` block" },
    { "a`]`", desc = "`[]` block" },
    { "a<", desc = "<> block" },
    { "a>", desc = "<> block" },

{ "i", group = "inside" },
{ "i'", desc = "inner ' string" },
{ 'i"', desc = 'inner " string' },
{ "iw", desc = "inner word" },
{ "iW", desc = "inner WORD" },
{ "ip", desc = "inner paragraph" },
{ "is", desc = "inner sentence" },
{ "it", desc = "inner tag block" },
{ "i`` ` ``", desc = "inner`` ` ``string" },
{ "ib", desc = "inner ()" },
{ "iB", desc = "inner `{}` },
{ "i(", desc = "inner `()` },
{ "i)", desc = "inner `()` },
{ "i{", desc = "inner {}" },
{ "i}", desc = "inner {}" },
{ "i[", desc = "inner []" },
{ "i]", desc = "inner []" },
{ "i<", desc = "inner <>" },
{ "i>", desc = "inner <>" },
    }

m -> **mark current position with a letter (e.g., ma)**

replace
r -> replace single character under cursor

single operation
**u** -> **undo last change**
**x** -> **delete character under cursor**
**X** -> **delete character before cursor**
**J** -> **join current line with next line**
**C** -> **change from cursor to end of line**
**D** -> **delete from cursor to end of line**

**P** -> **put (paste) before cursor/line**
**p** -> **put (paste) after cursor/line**
**N** -> **repeat last search in opposite direction**
**n** -> **repeat last search in same direction**

operators
**d** -> delete
**c** -> change
**y** -> yank (copy)

**~** -> swap case (only if 'tildeop' is set)
**g~** -> swap case
**gu** -> make lowercase
**gU** -> make uppercase
**!** -> filter through an external program
**=** -> filter through 'equalprg' or C-indenting if empty
**gq** -> text formatting
**gw** -> text formatting with no cursor movement
**g?** -> ROT13 encoding
**>** -> shift right
**<** -> shift left
**zf** -> define a fold
**g@** -> call function set with the 'operatorfunc' option

{ "V", desc = "Visual Line" },
{ "r", desc = "Replace" },
{ "v", desc = "Visual" },


**mode change**

  O
I   A
i   a
  o

**i** -> go to insert mode before current char
**a** -> go to insert mode after current char
**I** -> go to insert mode before current line (at first non-blank char)
**A** -> go to insert mode after current line (at end of line)
**O** -> go to insert mode on a new line above current line
**o** -> go to insert mode on a new line below current line

**scrolling**

**H** -> move cursor to **H**ome (top) line of the screen
**L** -> move cursor to **L**ast (bottom) line of the screen
**M** -> move cursor to **M**iddle line of the screen

  u
b   f
  d
**u** -> scroll **u**p (half screen) — *or* undo in normal mode (context dependent)
**d** -> scroll **d**own (half screen) — *or* delete in normal mode

**b** -> scroll **b**ackward (one full screen) — *or* move to previous word
**f** -> scroll **f**orward (one full screen) — *or* find character in line

note : its under control layer

---

`+` < = T _ h j k l o q s v w x | H J K L

windows
  mode = { "n", "x" },
  { "<c-w>", group = "window" },
      { "<c-w>+", desc = "Increase height" },
      { "<c-w>-", desc = "Decrease height" },
      { "<c-w><", desc = "Decrease width" },
      { "<c-w>=", desc = "Equally high and wide" },
      { "<c-w>>", desc = "Increase width" },
      { "<c-w>T", desc = "Break out into a new tab" },
      { "<c-w>_", desc = "Max out the height" },
      { "<c-w>|", desc = "Max out the width" },
      { "<c-w>h", desc = "Go to the left window" },
      { "<c-w>j", desc = "Go to the down window" },
      { "<c-w>k", desc = "Go to the up window" },
      { "<c-w>l", desc = "Go to the right window" },
      { "<c-w>o", desc = "Close all other windows" },
      { "<c-w>q", desc = "Quit a window" },
      { "<c-w>s", desc = "Split window" },
      { "<c-w>v", desc = "Split window vertically" },
      { "<c-w>w", desc = "Switch windows" },
      { "<c-w>x", desc = "Swap current with next" },
      { "<c-w>H", desc = "Move window to far left" },
      { "<c-w>J", desc = "Move window to far bottom" },
      { "<c-w>K", desc = "Move window to far top" },
      { "<c-w>L", desc = "Move window to far right" },
}


  <CR> = A C D E H L M O R a b c d e g i m o r s t v w x z

M.z = {
  preset = true,
  { "z<CR>", desc = "Top this line" },
  { "zo", desc = "Open fold under cursor" },
  { "zO", desc = "Open all folds under cursor" },
  { "zc", desc = "Close fold under cursor" },
  { "zC", desc = "Close all folds under cursor" },
  { "zR", desc = "Open all folds" },
  { "zM", desc = "Close all folds" },
  { "zi", desc = "Toggle folding" },
  { "za", desc = "Toggle fold under cursor" },
  { "zA", desc = "Toggle all folds under cursor" },
  { "zd", desc = "Delete fold under cursor" },
  { "zD", desc = "Delete all folds under cursor" },
  { "zE", desc = "Delete all folds in file" },
  { "zH", desc = "Half screen to the left" },
  { "zL", desc = "Half screen to the right" },
  { "zm", desc = "Fold more" },
  { "zr", desc = "Fold less" },
  { "zv", desc = "Show cursor line" },
  { "zg", desc = "Add word to spell list" },
  { "z=", desc = "Spelling suggestions" },
  { "zw", desc = "Mark word as bad/misspelling" },
  { "zx", desc = "Update folds" },
  { "zs", desc = "Left this line" },
  { "ze", desc = "Right this line" },
  { "zt", desc = "Top this line" },
  { "zz", desc = "Center this line" },
  { "zb", desc = "Bottom this line" },
}

nav
  { "H", desc = "Home line of window (top)" },
  { "L", desc = "Last line of window" },
  { "M", desc = "Middle line of window" },


{ "`[%`", desc = "Previous unmatched group" },
{ "`]%`", desc = "Next unmatched group" },

{ "`[(`", desc = "Previous (" },
{ "`](`", desc = "Next (" },

{ "`[<`", desc = "Previous <" },
{ "`]<`", desc = "Next <" },

{ "`[m`", desc = "Previous method start" },
{ "`]m`", desc = "Next method start" },
{ "`[M`", desc = "Previous method end" },
{ "`]M`", desc = "Next method end" },
{ "`[s`", desc = "Previous misspelled word" },
{ "`]s`", desc = "Next misspelled word" },

{ "`[{`", desc = "Previous {" },
{ "`]{`", desc = "Next {" },

M.g = {
  { "g%", desc = "Cycle backwards through results" },

  { "g,", desc = "Go to `[count]`newer position in change list" },
  { "g;", desc = "Go to `[count]` older position in change list" },

  { "gn", desc = "Search forwards and select" },
  { "gN", desc = "Search backwards and select" },

  { "gT", desc = "Go to previous tab page" },
  { "gt", desc = "Go to next tab page" },

  { "gf", desc = "Go to file under cursor" },
  { "gi", desc = "Go to last insert" },
  { "gv", desc = "Last visual selection" },
  { "gx", desc = "Open file with system app" },
}

CTRL-@                  not used
<BS>                 1  same as "h"
<Tab>                1  go to N newer entry in jump list
<NL>                 1  same as "j"
<CR>                 1  cursor to the first CHAR N lines lower
<S-CR>               1  same as CTRL-F
<S-NL>               1  same as CTRL-F
<Space>              1  same as "l"

'{a-zA-Z0-9}         1  cursor to the first CHAR on the line with mark {a-zA-Z0-9}
''                   1  cursor to the first CHAR of the line where the cursor was before the latest jump.
'(                   1  cursor to the first CHAR on the line of the start of the current sentence
')                   1  cursor to the first CHAR on the line of the end of the current sentence
'`[`                 1  cursor to the first CHAR on the line of the start of last operated text or start of put text
'`]`                 1  cursor to the first CHAR on the line of the end of last operated text or end of put text
'{                   1  cursor to the first CHAR on the line of the start of the current paragraph
'}                   1  cursor to the first CHAR on the line of the end of the current paragraph
'<                   1  cursor to the first CHAR of the line where highlighted area starts/started in the current buffer.
'>                   1  cursor to the first CHAR of the line where highlighted area ends/ended in the current buffer.

`#`                  1  search backward for the Nth occurrence of the ident under the cursor
`*`                  1  search forward for the Nth occurrence of the ident under the cursor
%                    1  find the next (curly/square) bracket on this line and go to its match, or go to matching comment bracket, or go to matching preprocessor directive.
{count}%             1  go to N percentage in the file
0                    1  cursor to the first char of the line
^                    1  cursor to the first CHAR of the line
$                    1  cursor to the end of Nth next line
_                    1  cursor to the first CHAR N - 1 lines lower
(                    1  cursor N sentences backward
)                    1  cursor N sentences forward
{                    1  cursor N paragraphs backward
}                    1  cursor N paragraphs forward
|                    1  cursor to column N
`+`                  1  same as <CR>
`-`                  1  cursor to the first CHAR N lines higher
<S-+>                1  same as CTRL-F
<S-->                1  same as CTRL-B

!{motion}{filter}    2  filter Nmove text through the {filter} command
!!{filter}	         2  filter N lines through the {filter} command
&                    2  repeat last :s
"{register}             use {register} for next delete, yank or put ({.%#:} only work with put)
~                    2  'tildeop' off: switch case of N characters under cursor and move the cursor N characters to the right
`<<`                 2  shift N lines one 'shiftwidth' leftwards
`>>`                 2  shift N lines one 'shiftwidth' rightwards
`==`                 2  filter N lines through "indent"
`<`{motion}          2  shift Nmove lines one 'shiftwidth' leftwards
`=`{motion}          2  filter Nmove lines through "indent"
`>`{motion}          2  shift Nmove lines one 'shiftwidth' rightwards
`~`{motion}             'tildeop' on: switch case of Nmove text

/<CR>                1  search forward for {pattern} of last search
/{pattern}<CR>       1  search forward for the Nth occurrence of {pattern}
?<CR>                1  search backward for {pattern} of last search
?{pattern}<CR>       1  search backward for the Nth previous occurrence of {pattern}

@{a-z}               2  execute the contents of register {a-z} N times
@:                      repeat the previous ":" command N times
@@                   2  repeat the previous @{a-z} N times

`\`                     not used
`[`{char}               square bracket command (see `[` below)
`]`{char}               square bracket command (see `]` below)

{'a-zA-Z0-9}         1  cursor to the mark {a-zA-Z0-9}
`` `(``                1  cursor to the start of the current sentence
`` `)``                1  cursor to the end of the current sentence
`` `<``                1  cursor to the start of the highlighted area
`` `>``                1  cursor to the end of the highlighted area
`` `[``                1  cursor to the start of last operated text or start of putted text
`` `] ``               1  cursor to the end of last operated text or end of putted text
``` `` ```               1  cursor to the position before latest jump
`` `{ ``               1  cursor to the start of the current paragraph
`` `} ``               1  cursor to the end of the current paragraph

CTRL-`[` <Esc>          not used
CTRL-\ a - z            reserved for extensions
CTRL-\ CTRL-N           go to Normal mode (no-op)
CTRL-\ CTRL-G           go to Normal mode (no-op)
CTRL-\ others           not used
CTRL-]                  :ta to ident under cursor
CTRL-^                  edit Nth alternate file (equivalent to ":e #N")
CTRL-<Tab>              same as g<Tab> : go to last accessed tab page
CTRL-_                  not used

CTRL-E                  scroll N lines upwards (N lines Extra)
CTRL-Y                  scroll N lines downwards
CTRL-B               1  scroll N screens Backwards
CTRL-F               1  scroll N screens Forward
CTRL-U                  scroll N lines Upwards (default: half a screen)
CTRL-D                  scroll Down N lines (default: half a screen)

CTRL-H               1  same as "h"
CTRL-J               1  same as "j"
CTRL-N               1  same as "j"
CTRL-P               1  same as "k"
CTRL-M               1  same as <CR>
CTRL-I               1  same as <Tab>
CTRL-C                  interrupt current (search) command
CTRL-Z                  suspend program (or start new shell)
CTRL-A               2  add N to number at/after cursor
CTRL-X               2  subtract N from number at/after cursor
CTRL-G                  display current file name and position
CTRL-L                  redraw screen
CTRL-O               1  go to N older entry in jump list
CTRL-K                  not used
CTRL-Q                  not used, or used for terminal control flow
CTRL-S                  not used, or used for terminal control flow
CTRL-R               2  redo changes which were undone with 'u'
CTRL-T                  jump to N older Tag in tag list
CTRL-V                  start blockwise Visual mode

CTRL-W +                increase current window height N lines
CTRL-W -                decrease current window height N lines
CTRL-W <                decrease current window width N columns
CTRL-W >                increase current window width N columns
CTRL-W =                make all windows the same height & width

CTRL-W h                go to Nth left window (stop at first window)
CTRL-W H                move current window to the far left
CTRL-W CTRL-H           same as "CTRL-W h"
CTRL-W <Left>           same as "CTRL-W h"
CTRL-W j                go N windows down (stop at last window)
CTRL-W J                move current window to the very bottom
CTRL-W CTRL-J           same as "CTRL-W j"
CTRL-W <Down>           same as "CTRL-W j"
CTRL-W k                go N windows up (stop at first window)
CTRL-W K                move current window to the very top
CTRL-W CTRL-K           same as "CTRL-W k"
CTRL-W <Up>             same as "CTRL-W k"
CTRL-W l                go to Nth right window (stop at last window)
CTRL-W L                move current window to the far right
CTRL-W CTRL-L           same as "CTRL-W l"
CTRL-W <Right>          same as "CTRL-W l"

CTRL-W i                split window and jump to declaration of identifier under the cursor
CTRL-W CTRL-I           same as "CTRL-W i"
CTRL-W P                go to preview window
CTRL-W CTRL-P           same as "CTRL-W p"
CTRL-W R                rotate windows upwards N times
CTRL-W CTRL-R           same as "CTRL-W r"
CTRL-W S                same as "CTRL-W s"
CTRL-W CTRL-S           same as "CTRL-W s"
CTRL-W T                move current window to a new tab page
CTRL-W W                go to N previous window (wrap around)
CTRL-W c                close current window (like :close)
CTRL-W CTRL-C           no-op
CTRL-W b                go to bottom window
CTRL-W CTRL-B           same as "CTRL-W b"

CTRL-W d                split window and jump to definition under the cursor
CTRL-W CTRL-D           same as "CTRL-W d"
CTRL-W f                split window and edit file name under the cursor
CTRL-W CTRL-F           same as "CTRL-W f"
CTRL-W F                split window and edit file name under the cursor and jump to the line number following the file name.
CTRL-W n                open new window, N lines high
CTRL-W CTRL-N           same as "CTRL-W n"
CTRL-W o                close all but current window (like :only)
CTRL-W CTRL-O           same as "CTRL-W o"
CTRL-W p                go to previous (last accessed) window
CTRL-W q                quit current window (like :quit)
CTRL-W CTRL-Q           same as "CTRL-W q"
CTRL-W r                rotate windows downwards N times
CTRL-W s                split current window in two parts, new window N lines high
CTRL-W t                go to top window
CTRL-W CTRL-T           same as "CTRL-W t"
CTRL-W v                split current window vertically, new window N columns wide
CTRL-W CTRL-V           same as "CTRL-W v"
CTRL-W w                go to N next window (wrap around)
CTRL-W CTRL-W           same as "CTRL-W w"
CTRL-W x                exchange current window with window N (default: next window)
CTRL-W CTRL-X           same as "CTRL-W x"
CTRL-W z                close preview window
CTRL-W CTRL-Z           same as "CTRL-W z"

CTRL-W g CTRL-]         split window and do :tjump to tag under cursor
CTRL-W g ]              split window and do :tselect for tag under cursor
CTRL-W g }              do a :ptjump to the tag under the cursor
CTRL-W g f              edit file name under the cursor in a new tab page
CTRL-W g F              edit file name under the cursor in a new tab page and jump to the line number following the file name.
CTRL-W g t              same as gt: go to next tab page
CTRL-W g T              same as gT: go to previous tab page
CTRL-W g <Tab>          same as g<Tab>: go to last accessed tab page
CTRL-W CTRL-G           same as "CTRL-W g .."

CTRL-W ]                split window and jump to tag under cursor
CTRL-W CTRL-]           same as "CTRL-W ]"
CTRL-W ^                split current window and edit alternate file N
CTRL-W CTRL-^           same as "CTRL-W ^"
CTRL-W _                set current window height to N (default: very high)
CTRL-W CTRL-_           same as "CTRL-W _"
CTRL-W |                set window width to N columns
CTRL-W }                show tag under cursor in preview window

`["x]`x              2  delete N characters under and after the cursor `[into register x]`
`["x]`X              2  delete N characters before the cursor `[into register x]`
`["x]`c{motion}      2  delete Nmove text `[into register x]` and start insert
`["x]`C              2  change from the cursor position to the end of the line, and N-1 more lines `[into register x]`; synonym for "c$"
`["x]`cc             2  delete N lines `[into register x]` and start insert
`["x]`d{motion}      2  delete Nmove text `[into register x]`
`["x]`D              2  delete the characters under the cursor until the end of the line and N-1 more lines `[into register x]` synonym for "d$"
`["x]`dd             2  delete N lines `[into register x]`
`["x]`p              2  put the text `[from register x]` after the cursor N times
`["x]`P              2  put the text `[from register x]` before the cursor N times
`["x]`s              2  (substitute) delete N characters `[into register x]` and start insert
`["x]`S              2  delete N lines `[into register x]` and start insert; synonym for "cc".
`["x]`y{motion}         yank N move text `[into register x]`
`["x]`yy                yank N lines `[into register x]`
`["x]`Y                 yank N lines `[into register x]`; synonym for "yy" Note: Mapped to "y$" by default. default-mappings

m{A-Za-z}               set mark {A-Za-z} at cursor position
q{0-9a-zA-Z"}           record typed characters into named register {0-9a-zA-Z"} (uppercase to append)

f{char}              1  cursor to Nth occurrence of {char} to the right
F{char}              1  cursor to the Nth occurrence of {char} to the left
t{char}              1  cursor till before Nth occurrence of {char} to the right
T{char}              1  cursor till after Nth occurrence of {char} to the left
r{char}              2  replace N chars with {char}
R                    2  enter replace mode: overtype existing characters, repeat the entered text N-1 times

g{char}                 extended commands, see g below
z{char}                 commands starting with 'z', see z below

a                    2  append text after the cursor N times
i                    2  insert text before the cursor N times
o                    2  begin a new line below the cursor and insert text, repeat N times
v                       start charwise Visual mode
A                    2  append text after the end of the line N times
I                    2  insert text before the first CHAR on the line N times
O                    2  begin a new line above the cursor and insert text, repeat N times
V                       start linewise Visual mode

w                    1  cursor N words forward
b                    1  cursor N words backward
e                    1  cursor forward to the end of word N
h                    1  cursor N chars to the left
j                    1  cursor N lines downward
k                    1  cursor N lines upward
l                    1  cursor N chars to the right
W                    1  cursor N WORDS forward
E                    1  cursor forward to the end of WORD N
B                    1  cursor N WORDS backward
H                    1  cursor to line N from top of screen
M                    1  cursor to middle line of screen
L                    1  cursor to line N from bottom of screen

J                    2  Join N lines; default is 2
K                       lookup Keyword under the cursor with 'keywordprg'
U                    2  undo all latest changes on one line
ZZ                      write if buffer changed and close window
ZQ                      close window without writing

u                    2  undo changes
do                   2  same as ":diffget"
dp                   2  same as ":diffput"

,                    1  repeat latest f, t, F or T in opposite direction N times
;                    1  repeat latest f, t, F or T N times
.                    2  repeat last change with count replaced with N
:                    1  start entering an Ex command
{count}:                start entering an Ex command with range from current line to N-1 lines down
n                    1  repeat the latest '/' or '?' N times
N                    1  repeat the latest '/' or '?' N times in opposite direction
q                       (while recording) stops recording
Q                    2  replay last recorded register
q:                      edit : command-line in command-line window
q/                      edit / command-line in command-line window
q?                      edit ? command-line in command-line window

"x<Del>              2  same as "x"
N<Del>                  remove the last digit from {count}

<F1>                    same as <Help>
<Help>                  open a help window
<Insert>             2  same as "i"

<Up>                 1  same as "k"
<Down>               1  same as "j"
<Left>               1  same as "h"
<Right>              1  same as "l"
<C-Left>             1  same as "b"
<C-Right>            1  same as "w"
<S-Left>             1  same as "b"
<S-Right>            1  same as "w"
<S-Up>               1  same as CTRL-B
<S-Down>             1  same as CTRL-F
<PageUp>                same as CTRL-B
<PageDown>              same as CTRL-F

<Home>               1  same as "0"
<End>                1  same as "$"
<C-Home>             1  same as "gg"
<C-End>              1  same as "G"

<LeftMouse>          1  move cursor to the mouse click position
<MiddleMouse>        2  same as "gP" at the mouse click position
<RightMouse>            start Visual mode, move cursor to the mouse click position
<C-LeftMouse>           ":ta" to the keyword at the mouse click
<C-RightMouse>          same as "CTRL-T"
<S-LeftMouse>           same as "*" at the mouse click position
<S-RightMouse>          same as "#" at the mouse click position
<C-Tab>                 same as "g<Tab>"
<Undo>               2  same as "u"

<ScrollWheelUp>         move window three lines up
<ScrollWheelDown>       move window three lines down
<ScrollWheelLeft>       move window six columns left
<ScrollWheelRight>      move window six columns right
<S-ScrollWheelUp>       move window one page up
<S-ScrollWheelDown>     move window one page down
<S-ScrollWheelLeft>     move window one page left
<S-ScrollWheelRight>    move window one page right
