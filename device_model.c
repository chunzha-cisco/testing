#include <stdio.h>
#include <string.h>

struct DeviceMapping {
    const char *name;
    const char *model;
};

static struct DeviceMapping device_map[] = {
    {"iPhone10,1", "iPhone 8"},
    {"iPhone13,1", "iPhone 12 mini"},
    {"SM-G950F", "Samsung Galaxy S8"},
    {"SM-G973F", "Samsung Galaxy S10"},
    {"Pixel 5", "Google Pixel 5"},
};

static const int num_devices = sizeof(device_map) / sizeof(device_map[0]);

int main(void) {
    char input[100];

    printf("Enter device name: ");
    if (!fgets(input, sizeof(input), stdin)) {
        return 1;
    }

    /* remove potential trailing newline */
    input[strcspn(input, "\n")] = '\0';

    for (int i = 0; i < num_devices; ++i) {
        if (strcmp(device_map[i].name, input) == 0) {
            printf("Model: %s\n", device_map[i].model);
            return 0;
        }
    }

    printf("Model: Unknown device\n");
    return 0;
}
