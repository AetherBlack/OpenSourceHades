
#include "../hades.h"

void
hades_check_language(void)
{
    char *langue = getenv("LANG");

    if (!strncmp(langue, "en_US", 5) || !strncmp(langue, "fr_FR", 5)) {
        exit(0);
    }
    return;
}
