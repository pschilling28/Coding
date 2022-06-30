#include <iostream>
#include <vector>
#include "functions.hpp"

//global variables
std::vector<char> choices = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
std::string player1, player2;
int choice;
bool end_game = false;
int filled_spaces = 0;

//global functions
void game_board() {
    std::cout << "1     |2    |3     \n";
    std::cout << "   " << choices[0] << "  |  " << choices[1] << "  |  " << choices[2] << "   \n";
    std::cout << "______|_____|______\n";
    std::cout << "4     |5    |6     \n";
    std::cout << "   " << choices[3] << "  |  " << choices[4] << "  |  " << choices[5] << "   \n";
    std::cout << "______|_____|______\n";
    std::cout << "7     |8    |9     \n";
    std::cout << "   " << choices[6] << "  |  " << choices[7] << "  |  " << choices[8] << "   \n";
    std::cout << "      |     |      \n";
    std::cout << "\n";
}

void setup() {
    std::cout << "=======================\n";
    std::cout << "Welcome to Tic Tac Toe!\n";
    std::cout << "=======================\n";
    std::cout << "You know the rules, so play by alternating turns between two players.\n";
    std::cout << "Enter the number that corresponds to the space you are choosing (i.e. to take the upper left corner, enter 1.)\n";
    std::cout << "\n";
    std::cout << "Player 1 (the player that is going first, and will be represented by 'X') enter your name: ";
    std::cin >> player1;
    std::cout << "Player 2, you will be 'Y', enter your name: ";
    std::cin >> player2;
    std::cout << "\n";
    game_board();
}

void X_turn() {
    std::cout << player1 << ", pick a space.\n";
    std::cin >> choice;

    while (choices[choice - 1] != ' '){
        std::cout << "This space is already taken or you entered an invalid number. Try again.\n";
        game_board();
        std::cin >> choice;
    }
    choices[choice - 1] = 'X';
    filled_spaces++;
    game_board(); 
    check_winning_condition();
}

void O_turn() {
    std::cout << player2 << ", pick a space.\n";
    std::cin >> choice;

    while (choices[choice - 1] != ' '){
        std::cout << "This space is already taken or you entered an invalid number. Try again.\n";
        game_board();
        std::cin >> choice;
    }
    choices[choice - 1] = 'O';
    filled_spaces++;
    game_board(); 
    check_winning_condition();
}

void check_winning_condition() {
    //horizontal wins
    if (choices[0] != ' ' && choices[0] == choices[1] && choices[0] == choices[2]) {
        if (choices[0] == 'X') {
            std::cout << player1 << " wins!\n";
        } else {
            std::cout << player2 << " wins!\n";
        }
        end_game = true;
    } else if (choices[3] != ' ' && choices[3] == choices[4] && choices[3] == choices[5]) {
        if (choices[3] == 'X') {
            std::cout << player1 << " wins!\n";
        } else {
            std::cout << player2 << " wins!\n";
        }
        end_game = true;
    } else if (choices[6] != ' ' && choices[6] == choices[7] && choices[6] == choices[8]) {
        if (choices[6] == 'X') {
            std::cout << player1 << " wins!\n";
        } else {
            std::cout << player2 << " wins!\n";
        }
        end_game = true;
    //vertical wins
    } else if (choices[0] != ' ' && choices[0] == choices[3] && choices[0] == choices[6]) {
        if (choices[0] == 'X') {
            std::cout << player1 << " wins!\n";
        } else {
            std::cout << player2 << " wins!\n";
        }
        end_game = true;
    } else if (choices[1] != ' ' && choices[1] == choices[4] && choices[1] == choices[7]) {
        if (choices[1] == 'X') {
            std::cout << player1 << " wins!\n";
        } else {
            std::cout << player2 << " wins!\n";
        }
        end_game = true;
    } else if (choices[2] != ' ' && choices[2] == choices[5] && choices[2] == choices[8]) {
        if (choices[2] == 'X') {
            std::cout << player1 << " wins!\n";
        } else {
            std::cout << player2 << " wins!\n";
        }
        end_game = true;
    //diagonal wins
    } else if (choices[0] != ' ' && choices[0] == choices[4] && choices[0] == choices[8]) {
        if (choices[0] == 'X') {
            std::cout << player1 << " wins!\n";
        } else {
            std::cout << player2 << " wins!\n";
        }
        end_game = true;
    } else if (choices[2] != ' ' && choices[2] == choices[4] && choices[2] == choices[6]) {
        if (choices[2] == 'X') {
            std::cout << player1 << " wins!\n";
        } else {
            std::cout << player2 << " wins!\n";
        }
        end_game = true;
    } else if (filled_spaces == 9) {
        std::cout << "Game is a tie!\n";
        end_game = true;
    }   
}

void play_game() {
    while (end_game == false) {
        X_turn();
        if (end_game == false) {
            O_turn();
        }
    }
}