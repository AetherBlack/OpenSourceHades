
#include "../hades.h"

char **hades_directory_files(char *directory)
{
    int filecount;

    DIR *dptr = opendir(".");
    struct dirent *dir;

    if (dptr == NULL) {
        exit(0);
    }

    while ((dir = readdir(dptr)) != NULL) {
        if (dir->d_type == DT_REG) {
            filecount++;
        }
    }

    char **files = malloc(filecount * sizeof(char *));

    rewinddir(dptr);

    int k = 0;
    while ((dir = readdir(dptr)) != NULL) {
        if (dir->d_type == DT_REG) {
            files[k] = malloc(strlen(dir->d_name) + 1);
            strcpy(files[k], dir->d_name);
            k++;
        }
    }

    closedir(dptr);

    return files;
}