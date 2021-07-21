#include <iostream>
#include <string>

constexpr int n = 300;
int mem[n + 1][n + 1][n + 1];

int total_power(int x, int y, int s) {
    if (s == 1) {
        return mem[x][y][1];
    }

    int total = mem[x][y][s - 1] + mem[x + 1][y + 1][s - 1]
                + mem[x + s - 1][y][1 ]+ mem[x][y + s - 1][1]
                - mem[x + 1][y + 1][s - 2];
    mem[x][y][s] = total;
    return total;
}

int main(int argc, char *argv[]) {
    const int serial = (argc == 2) ? std::stoi(argv[1]) : 9005;

    for (int x = 1; x <= n; ++x) {
        for (int y = 1; y <= n; ++y) {
            int rack = x + 10;
            mem[x][y][1] = ((rack * y + serial) * rack) / 100 % 10 - 5;
        }
    }

    int mx, my, ms, mt, mx3, my3, mt3;
    mx = my = ms = mt = mx3 = my3 = mt3 = 0;
    for (int s = 1; s <= n; ++s) {
        for (int x = 1; x <= n - s + 1; ++x) {
            for (int y = 1; y <= n - s + 1; ++y) {
                int total = total_power(x, y, s);
                //std::cout << s << " " << x << " " << y << " " << total << std::endl;
                if (s == 3 && total > mt3) {
                    mx3 = x;
                    my3 = y;
                    mt3 = total;
                } else if (total > mt) {
                    mx = x;
                    my = y;
                    ms = s;
                    mt = total;
                }
            }
        }
    }

    std::cout << mx3 << "," << my3 << " " << mx << "," << my << "," << ms << " " << std::endl;
}
