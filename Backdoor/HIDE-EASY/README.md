https://backdoor.sdslabs.co/challenges/HIDE-EASY

```
$ wget http://hack.bckdr.in/HIDE-EASY/hide_easy
$ file hide_easy
hide_easy: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=cf56f38a7483f0f337aa3b25644426028885c9b9, not stripped
$ strings hide_easy
/lib/ld-linux.so.2
;%dD&
libc.so.6
_IO_stdin_used
puts
printf
__libc_start_main
__gmon_start__
GLIBC_2.0
PTRh
QVhl
[^_]
939d9556640d4
47f5847d92e9fbbd4d762036ff684ccde6a80d3a171c4dcd0b724fae25826c36
What do you think you will get here?
;*2$"
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

Hmm, `47f5847d92e9fbbd4d762036ff684ccde6a80d3a171c4dcd0b724fae25826c36` sure looks like a hash.
