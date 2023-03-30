char ** environment() {
    extern char **environ;  // stores environment variables
    return environ;
}