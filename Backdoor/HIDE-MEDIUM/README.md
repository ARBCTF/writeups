https://backdoor.sdslabs.co/challenges/HIDE-MEDIUM

Alright, let's grab the file...

```
$ wget http://hack.bckdr.in/HIDE-MEDIUM/hide_medium
$ file hide_medium 
hide_medium: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=fe9ddc13d0659e1badb3fd04934d02b4aa60893a, not stripped
```

Ok, so it's a binary.

```
$ strings hide_medium 
/lib/ld-linux.so.2
libc.so.6
_IO_stdin_used
puts
__stack_chk_fail
printf
__libc_start_main
__gmon_start__
GLIBC_2.4
GLIBC_2.0
PTRh
QVhq
l[^_]
[^_]
KI!!
It's not that easy as you think so
;*2$"(
GCC: (Ubuntu/Linaro 4.7.3-1ubuntu1) 4.7.3
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.jcr
.dynamic
.got
.got.plt
.data
.bss
.comment
crtstuff.c
__JCR_LIST__
deregister_tm_clones
register_tm_clones
__do_global_dtors_aux
completed.6339
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
code.c
__FRAME_END__
__JCR_END__
__init_array_end
_DYNAMIC
__init_array_start
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
__x86.get_pc_thunk.bx
data_start
printf@@GLIBC_2.0
_edata
_fini
__stack_chk_fail@@GLIBC_2.4
__data_start
puts@@GLIBC_2.0
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_start_main@@GLIBC_2.0
__libc_csu_init
_end
_start
_fp_hw
__bss_start
main
_Jv_RegisterClasses
print_flag
__TMC_END__
_ITM_registerTMCloneTable
_init
```

Cheeky: `It's not that easy as you think so`

But I also see `print_flag`.

If we run it through `objdump -D` it looks like `print_flag` is a function. Let's try and hit the function with GDB.

```
$ gdb -q hide_medium 
Reading symbols from hide_medium...(no debugging symbols found)...done.
(gdb) info address print_flag
Symbol "print_flag" is at 0x804849c in a file compiled without debugging.
(gdb) break main
Breakpoint 1 at 0x8048574
(gdb) run
Starting program: /home/matt/ctf/hide_medium 

Breakpoint 1, 0x08048574 in main ()
(gdb) set $eip = 0x804849c
(gdb) continue
Continuing.
<redacted>

Program received signal SIGSEGV, Segmentation fault.
0x00000000 in ?? ()
```

Got it.
