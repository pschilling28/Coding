#include <iostream>
#include <vector>
#include "functions.hpp"

std::string player_name;
int weight_class;
std::string background;

void intro_screen() {
    std::cout << "|                                                                                             |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                           W   W   AAA   N   N  N   N   AAA                                  |\n";
    std::cout << "|                           W   W  A   A  NN  N  NN  N  A   A                                 |\n";
    std::cout << "|                           W   W  A   A  N N N  N N N  A   A                                 |\n";
    std::cout << "|                           W W W  AAAAA  N  NN  N  NN  AAAAA                                 |\n";
    std::cout << "|                           WW WW  A   A  N   N  N   N  A   A                                 |\n";
    std::cout << "|                           WW WW  A   A  N   N  N   N  A   A                                 |\n";
    std::cout << "|                           W   W  A   A  N   N  N   N  A   A                                 |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                    W   W  RRRR   EEEEE   SSS   TTTTT  L      EEEEE   ???                    |\n";
    std::cout << "|                    W   W  R   R  E      S   S    T    L      E      ?   ?                   |\n";
    std::cout << "|                    W   W  R   R  E      S        T    L      E          ?                   |\n";
    std::cout << "|                    W W W  RRRR   EEEEE   SSS     T    L      EEEEE   ???                    |\n";
    std::cout << "|                    WW WW  R R    E          S    T    L      E        ?                     |\n";
    std::cout << "|                    WW WW  R  R   E      S   S    T    L      E                              |\n";
    std::cout << "|                    W   W  R   R  EEEEE   SSS     T    LLLLL  EEEEE    ?                     |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                           A HIGH SCHOOL-STYLE WRESTLING SIMULATION                          |\n";
    std::cout << "|                                    PRESS ENTER TO CONTINUE                                  |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                                                                                             |\n";
    std::cout << "|                                                                                             |\n";
    std::cin.ignore();
}

/*class Wrestler {
    public:
        std::string name, style, background;
        int weight_class, agility, strength, stamina, technique;
        std::vector<std::string> technique_list;
};*/

void coach_intro() {
    std::cout << "???: \"Welcome to the first day of practice, 9th-graders. My name is Pat. You can call me      \n";
    std::cout << "\'COACH\'\".                                                                                   \n";
    std::cout << "\n";
    std::cout << "                                                                        PRESS ENTER TO CONTINUE\n";
    std::cin.ignore();
    std::cout << "COACH: \"Wrestling is a grueling sport. And though we will have fun, we will also work very    \n";
    std::cout << "hard every practice to build your agility, strength, stamina, and technique.\"                 \n";
    std::cout << "\n";
    std::cout << "                                                                        PRESS ENTER TO CONTINUE\n";
    std::cin.ignore();
    std::cout << "COACH: \"First, I need to know more about my new squad! You there: tell us about yourself.\"   \n";
    std::cout << "\n";
    std::cout << "                                                                        PRESS ENTER TO CONTINUE\n";
    std::cin.ignore();
}

void name_wrestler() {
    char choice;
    std::cout << "???: \"... Well, my name is...\"\n";
    std::cout << "                                                              TYPE YOUR NAME, FOLLOWED BY ENTER\n";
    std::cin >> player_name;
    while (choice != 'Y' && choice != 'y') {
        std::cout << "COACH: \"" << player_name << ", is that right?\"\n";
        std::cout << "                                                             TYPE 'Y' OR 'N', FOLLOWED BY ENTER\n";
        std::cin >> choice;
        if (choice == 'N' || choice == 'n') {
            std::cout << "COACH: \"Oh, sorry. Cauliflower ear must be messing with my hearing. What is your name?\"\n";
            std::cout << "                                                              TYPE YOUR NAME, FOLLOWED BY ENTER\n";
            std::cin >> player_name;
        } else if (choice == 'Y' || choice == 'y') {
            break;
        } else {
            std::cout << "                                      INVALID CHOICE. TYPE EITHER 'Y' OR 'N', FOLLOWED BY ENTER\n";
            std::cout << "\n";
        }
    }
}

void choose_weight_class() {
    char choice;
    std::cout << "COACH: \"Alright, " << player_name << ", in what weight class do you plan to wrestle? In case  \n";
    std::cout << "you didn't know, there are fourteen weight classes this season. They are as follows in pounds: \n";
    std::cout << "106, 113, 120, 126, 132, 138, 145, 152, 160, 170, 182, 195, 220, 285.                          \n";
    std::cout << "                                                                                               \n";
    std::cout << "                                                                        PRESS ENTER TO CONTINUE\n";
    std::cin.ignore();
    std::cout << player_name << ": \"I think I can make...\"\n";
    std::cout << "                                                     CHOOSE YOUR WEIGHT CLASS, THEN PRESS ENTER\n";
    std::cin >> weight_class;
    while (choice != 'Y' && choice != 'y') {
        while (weight_class != 106 && weight_class != 113 && weight_class != 120 && weight_class != 126 && weight_class != 132 && weight_class != 138 && weight_class != 145 && weight_class != 152 && weight_class != 160 && weight_class != 170 && weight_class != 182 && weight_class != 195 && weight_class != 220 && weight_class != 285) {
            std::cout << "COACH: \"" << weight_class << " is not a weight class.\"\n";
            std::cout << "                                                                                               \n";
            std::cout << "CHOOSE ONE OF THE FOLLOWING WEIGHT CLASSES: 106, 113, 120, 126, 132, 138, 145, 152, 160, 170,  \n";
            std::cout << "182, 195, 220, 285.\n";
            std::cin >> weight_class;
        }
        std::cout << "COACH: \"" << weight_class << ", looks like you could make that. Are you sure?\"\n";
        std::cout << "                                                             TYPE 'Y' OR 'N', FOLLOWED BY ENTER\n";
        std::cin >> choice;
        if (choice == 'N' || choice == 'n') {
            std::cout << "COACH: \"Okay, then what weight class?\n";
            std::cout << "                                                                                               \n";
            std::cout << "CHOOSE ONE OF THE FOLLOWING WEIGHT CLASSES: 106, 113, 120, 126, 132, 138, 145, 152, 160, 170,  \n";
            std::cout << "182, 195, 220, 285.\n";
            std::cin >> weight_class;
        } else if (choice == 'Y' || choice == 'y') {
            break;
        } else {
            std::cout << "                                      INVALID CHOICE. TYPE EITHER 'Y' OR 'N', FOLLOWED BY ENTER\n";
            std::cout << "\n";
        }
    }
}

void choose_background() {
    char choice;
    std::cout << "COACH: \"Alright, " << player_name << ". I've got you jotted down for the " << weight_class << "-pound weight class.\"\n";
    std::cout << "                                                                        PRESS ENTER TO CONTINUE\n";
    std::cin.ignore();
    std::cout << "COACH: \"So tell me about yourself, " << player_name << ".\"\n";
    std::cout << "\n";
    std::cout << "YOU CAN CHOOSE FROM FIVE BACKGROUNDS: FREESTYLER, FUNK, MATRAT, THROWER, MUSCLER. TYPE THE NAME\n";
    std::cout << "OF ONE TO LEARN MORE.\n";
    std::cin >> background;
    while (choice != 'Y' && choice != 'y') {
        while (background != "FREESTYLER" && background != "FUNK" && background != "MATRAT" && background != "THROWER" && background != "MUSCLER" && background != "freestyler" && background != "funk" && background != "matrat" && background != "thrower" && background != "muscler" && background != "Freestyler" && background != "Funk" && background != "Matrat" && background != "Thrower" && background != "Muscler") {
            std::cout << player_name << ": \"Well, I'm mainly a " << background << ".\"\n";
            std::cout << "COACH: \"" << background << "? I don't know what that means.\"\n";
            std::cout << "                                                                                               \n";
            std::cout << "YOU CAN CHOOSE FROM FIVE BACKGROUNDS: FREESTYLER, FUNK, MATRAT, THROWER, MUSCLER. TYPE THE NAME\n";
            std::cout << "OF ONE TO LEARN MORE.\n";
            std::cin >> background;
        }
        if (background == "FREESTYLER" || background == "freestyler" || background == "Freestyler") {
            std::cout << "freestyler test, press Y or N";
            std::cin >> choice;
        } else if (background == "FUNK" || background == "funk" || background == "Funk") {
            std::cout << "funk test, press Y or N";
            std::cin >> choice;
        } else if (background == "MATRAT" || background == "matrat" || background == "Matrat") {
            std::cout << "matrat test, press Y or N";
            std::cin >> choice;
        } else if (background == "THROWER" || background == "thrower" || background == "Thrower") {
            std::cout << "thrower test, press Y or N";
            std::cin >> choice;
        } else if (background == "MUSCLER" || background == "muscler" || background == "Muscler") {
            std::cout << "muscler test, press Y or N";
            std::cin >> choice;
        } else {
            std::cout << "Error in code in choose_background";
        }
        if (choice == 'N' || choice == 'n') {
            std::cout << "COACH: \"Okay, then what weight class?\n";
            std::cout << "                                                                                               \n";
            std::cout << "YOU CAN CHOOSE FROM FIVE BACKGROUNDS: FREESTYLER, FUNK, MATRAT, THROWER, MUSCLER. TYPE THE NAME\n";
            std::cout << "OF ONE TO LEARN MORE.\n";
            std::cin >> background;
        } else if (choice == 'Y' || choice == 'y') {
            break;
        } else {
            std::cout << "                                      INVALID CHOICE. TYPE EITHER 'Y' OR 'N', FOLLOWED BY ENTER\n";
            std::cout << "\n";
        }
    }
}

void create_wrestler() {
    name_wrestler();
    choose_weight_class();
    choose_background();
}

void test_function() {
    //name_wrestler();
    choose_background();
}