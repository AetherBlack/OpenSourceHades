
#include "../hades.h"

void
hades_check_debug(void)
{
    if (ptrace(PTRACE_TRACEME, 0, NULL, 0) == -1) {
        exit(0);
    }
}