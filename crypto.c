#include<stdio.h>
#include<string.h>

#define MAX_SIZE 100

void display_matrix_format(unsigned char disp_message[MAX_SIZE][MAX_SIZE],int value);

int main()
{
    unsigned char ch, name[MAX_SIZE], plain_text[MAX_SIZE][MAX_SIZE], cipher[MAX_SIZE][MAX_SIZE], sec_key[MAX_SIZE][MAX_SIZE];
    unsigned int n, i, j, k, matrix_format, matrix_value, temp, flag = 0;
    unsigned char temp_sec_key[MAX_SIZE * MAX_SIZE];
    int name_index = 0;
    int key_index = 0; // Moved the declaration of key_index here

    printf("Enter the message in capital letters (max %d):\n", MAX_SIZE - 1);
    do
    {
        ch = getchar();
        if (name_index < MAX_SIZE - 1) {
            name[name_index] = ch;
            name_index++;
        }
    } while (ch != '\n');
    name[name_index - 1] = '\0'; // Null-terminate the string
    n = strlen(name);
    printf("String length is %d\n", n);

    if (n <= 4) {
        matrix_format = 2;
    } else if (n <= 9) {
        matrix_format = 3;
    } else if (n <= 16) {
        matrix_format = 4;
    } else if (n < 32) {
        matrix_format = 5;
    } else {
        printf("Message too long for current implementation (max 31 characters).\n");
        return 1;
    }

    name_index = 0;
    for (i = 0; i < matrix_format; i++) {
        for (j = 0; j < matrix_format; j++) {
            if (name_index < n) {
                plain_text[i][j] = (name[name_index] - 'A');
                name_index++;
            } else {
                plain_text[i][j] = ('Z' - 'A'); // Pad with 'Z'
            }
        }
    }

    printf("Plain Text Matrix:\n");
    display_matrix_format(plain_text, matrix_format);

    temp = matrix_format;
    matrix_value = matrix_format * matrix_format;
    printf("Matrix format is %d x %d\n", temp, temp);
    printf("Enter the encryption key within %d characters:\n", matrix_value);

    // key_index = 0; // Removed the redeclaration here
    do
    {
        ch = getchar();
        if (key_index < matrix_value) {
            temp_sec_key[key_index] = ch;
            key_index++;
        }
    } while (ch != '\n' && key_index < matrix_value);

    while (key_index < matrix_value)
    {
        temp_sec_key[key_index] = 'Z';
        key_index++;
    }

    key_index = 0;
    for (i = 0; i < matrix_format; i++) {
        for (j = 0; j < matrix_format; j++) {
            sec_key[i][j] = (temp_sec_key[key_index] - 'A');
            key_index++;
        }
    }

    printf("Secret Key Matrix:\n");
    display_matrix_format(sec_key, matrix_format);

    for (i = 0; i < matrix_format; i++) {
        for (j = 0; j < matrix_format; j++) {
            cipher[i][j] = 0;
            for (k = 0; k < matrix_format; k++) {
                cipher[i][j] += plain_text[i][k] * sec_key[k][j];
            }
            cipher[i][j] %= 26;
        }
    }

    printf("Cipher text is:\n");
    display_matrix_format(cipher, matrix_format);

    return 0;
}

void display_matrix_format(unsigned char disp_message[MAX_SIZE][MAX_SIZE], int value)
{
    int a, b;
    for (a = 0; a < value; a++) {
        for (b = 0; b < value; b++) {
            printf("%d\t", disp_message[a][b]);
        }
        printf("\n");
    }
}
