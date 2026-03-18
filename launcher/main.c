/*
 * tune-shifter launcher
 *
 * A minimal C binary that embeds Python and runs `python -m tune_shifter`.
 * Because this binary stays alive as the top-level process (no exec), macOS
 * sets p_comm to "tune-shifter" at exec time and it never changes — so both
 * Activity Monitor and `ps` show the correct name without any userspace tricks.
 *
 * Build (handled by the Homebrew formula):
 *   cc launcher/main.c \
 *     -DVENV_PYTHON='"<venv>/bin/python3"' \
 *     $(python3-config --cflags) \
 *     $(python3-config --ldflags --embed) \
 *     -Wno-deprecated-declarations \
 *     -o tune-shifter
 *
 * VENV_PYTHON tells Python which prefix/site-packages to use so the venv's
 * packages are importable even though the binary lives outside the venv.
 */

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

#ifndef VENV_PYTHON
#error "compile with -DVENV_PYTHON='\"<path-to-venv-python3>\"'"
#endif

int main(int argc, char *argv[]) {
    /* Tell Python which interpreter prefix to use — picks up venv site-packages. */
    wchar_t *program = Py_DecodeLocale(VENV_PYTHON, NULL);
    if (program == NULL) {
        fprintf(stderr, "tune-shifter: Py_DecodeLocale failed\n");
        return 1;
    }
    Py_SetProgramName(program);

    /*
     * Inject "-m tune_shifter" after argv[0] so the effect is:
     *   tune-shifter [user args]  →  python -m tune_shifter [user args]
     */
    int new_argc = argc + 2;
    char **new_argv = malloc((size_t)(new_argc + 1) * sizeof(char *));
    if (new_argv == NULL) {
        PyMem_RawFree(program);
        return 1;
    }
    new_argv[0] = argv[0];
    new_argv[1] = "-m";
    new_argv[2] = "tune_shifter";
    for (int i = 1; i < argc; i++) {
        new_argv[i + 2] = argv[i];
    }
    new_argv[new_argc] = NULL;

    int rc = Py_Main(new_argc, new_argv);

    free(new_argv);
    PyMem_RawFree(program);
    return rc;
}
