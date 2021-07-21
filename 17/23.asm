section .text
global simu
simu:
    push rbx
    push r12

    xor rax, rax
    xor rbx, rbx
    xor rcx, rcx
    xor r10, r10
    xor rdi, rdi
    xor rsi, rsi
    xor rax, rax
    xor r9, r9
    xor r12, r12
    mov r11, 100

    mov rbx, 65
    mov rcx, rbx
    test rax, rax
    ;jz .b ; part 1

    mov rax, rbx
    mul r11
    add r12, 1
    mov rbx, rax
    xor rax, rax

    sub rbx, -100000
    mov rcx, rbx
    sub rcx, -17000
.b:
    mov rsi, 1
    mov r10, 2
.h:
    mov rdi, 2
.d:
    mov rax, r10

    mul rdi
    ;add r12, 1

    sub rax, rbx
    test rax, rax
    jnz .c
    xor rsi, rsi
.c:
    sub rdi, -1
    mov rax, rdi
    sub rax, rbx
    test rax, rax
    jnz .d
    sub r10, -1
    mov rax, r10
    sub rax, rbx
    test rax, rax
    jnz .h
    test rsi, rsi
    jnz .e
    sub r9, -1
.e:
    mov rax, rbx
    sub rax, rcx
    test rax, rax
    jz .g
.f:
    sub rbx, -17
    jmp .b
.g:
    ;mov rax, r12 ; part 1
    mov rax, r9 ; part 2

    pop r12
    pop rbx
    ret
