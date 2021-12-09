#include <algorithm>
#include <cmath>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

bool isValid(int rows, int cols, int i, int j) {
    return (i >= 0 && i < rows && j >= 0 && j < cols);
}

vector<vector<int>> readFile() {
    /* Read input */

    if (!filesystem::exists("input.txt")) {
        cout << "input file does not exist" << endl;
        exit(1);
    }

    ifstream input("input.txt");

    /* Read data */
    vector<vector<int>> in;
    string s;

    while (!input.eof()) {
        vector<int> curr;
        getline(input, s);
        for (auto x : s) {
            curr.push_back(x - '0');
        }
        in.push_back(curr);
    }
    return in;
}

vector<pair<int, int>> part1(vector<vector<int>> &map) {
    int rows = map.size();
    int cols = map[0].size();

    vector<pair<int, int>> directions{{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    vector<pair<int, int>> lowPoints;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            bool low = true;
            for (int k = 0; k < directions.size(); k++) {
                int newI = directions[k].first;
                int newJ = directions[k].second;
                if (isValid(rows, cols, i + newI, j + newJ) &&
                    map[i][j] >= map[i + newI][j + newJ]) {
                    low = false;
                }
            }
            if (low) {
                lowPoints.push_back({i, j});
            }
        }
    }
    int sum = 0;
    for (auto x : lowPoints) {
        sum += map[x.first][x.second] + 1;
    }
    cout << sum << endl;
    return lowPoints;
}

void part2(vector<vector<int>> map, vector<pair<int, int>> lowPoints) {
    int rows = map.size();
    int cols = map[0].size();
    int sum = 0;
    vector<int> counts;
    vector<pair<int, int>> directions{{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    // BFS
    for (auto pnt : lowPoints) {
        queue<pair<int, int>> q;
        int crt = 1;
        vector<vector<int>> visited(rows, vector<int>(cols, 0));
        q.push(pnt);
        visited[pnt.first][pnt.second] = 1;
        while (!q.empty()) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            for (auto i = 0; i < directions.size(); i++) {
                int newX = directions[i].first;
                int newY = directions[i].second;
                if (isValid(rows, cols, x + newX, y + newY) &&
                    map[x][y] < map[x + newX][y + newY] &&
                    map[x + newX][y + newY] != 9 &&
                    !visited[x + newX][y + newY]) {
                    q.push({x + newX, y + newY});
                    visited[x + newX][y + newY] = 1;
                    crt++;
                }
            }
        }
        counts.push_back(crt);
    }
    sort(counts.begin(), counts.end(), greater<int>());
    int mul = 1;
    for (int i = 0; i < 3; i++) {
        mul *= counts[i];
    }
    cout << mul << endl;
}

int main() {
    string s;
    vector<vector<int>> map;
    vector<pair<int, int>> lowPoints;
    map = readFile();
    lowPoints = part1(map);
    part2(map, lowPoints);
}