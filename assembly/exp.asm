; code for A + (B - C)

section     .text
global      _start                              ;must be declared for linker (ld)

_start:                                         ;tell linker entry point

    mov     rax,[B]                         
    sub     rax,[C]                            
    mov     [temp0], rax

    mov     rax,[A]                         
    add     rax,[temp0]                            
    mov     [temp1], rax

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
