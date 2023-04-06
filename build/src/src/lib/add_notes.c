
#include "../hades.h"

/*
* 1. Create a note in $HOME directory
* 2. Create a note in current working directory
*/
void
hades_add_notes(void)
{
    /* Create two*/
    char *home_folder = getenv("HOME");
    int lhome_folder = strlen(home_folder);
    
    char *cwd = getcwd(NULL, 1024);
    int lcwd = strlen(cwd);

    char *home_note_file = (char *)malloc(lhome_folder + strlen(NOTE_NAME) + 1);
    char *cwd_note_file = (char *)malloc(lcwd + strlen(NOTE_NAME) + 1);

    /* $HOME/NOTE_NAME */
    strncpy(home_note_file, home_folder, lhome_folder);
    strncat(home_note_file, DELIMITOR, strlen(DELIMITOR) + 1);
    strncat(home_note_file, NOTE_NAME, strlen(NOTE_NAME) + 1);

    /* cwd()/NOTE_NAME */
    strncpy(cwd_note_file, cwd, lcwd);
    strncat(cwd_note_file, DELIMITOR, strlen(DELIMITOR) + 1);
    strncat(cwd_note_file, NOTE_NAME, strlen(NOTE_NAME) + 1);

    FILE *fptr_home = fopen(home_note_file, "w");
    FILE *fptr_cwd = fopen(cwd_note_file, "w");

    if (fptr_home != NULL) {
        fwrite(NOTE_CONTENT, 1, sizeof(NOTE_CONTENT), fptr_home);
        fclose(fptr_home);
    }
    if (fptr_cwd != NULL) {
        fwrite(NOTE_CONTENT, 1, sizeof(NOTE_CONTENT), fptr_cwd);
        fclose(fptr_cwd);
    }
}