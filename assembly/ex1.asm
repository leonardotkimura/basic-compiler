section     .text
global      _start                              ;must be declared for linker (ld)
_start:
mov     rax,[A]
div     qword [A]
mov     [temp0], rax
mov     rax,[B]
mul      qword [C]
mov     [temp1], rax
mov     rax,[B]
add     rax,[temp1]
mov     [temp2], rax
mov     rax,[temp0]
sub     rax,[temp2]
mov     [temp3], rax
_end:
int     0x80                                ;call kernel
section     .data
temp0       dd  0
temp1       dd  0
temp2       dd  0
temp3       dd  0
temp4       dd  0
temp5       dd  0
temp6       dd  0
temp7       dd  0
temp8       dd  0
temp9       dd  0
A           dd  100
B           dd  50
C           dd  20
