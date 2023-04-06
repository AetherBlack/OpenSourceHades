
#include "../hades.h"

void
hades_autodelete(char *filename)
{
    char *cwd = getcwd(NULL, 1024);
    chdir(cwd);

    char *sargs[] = {SHRED_CMD, filename, NULL};

    execvp(SHRED_CMD, sargs);
}