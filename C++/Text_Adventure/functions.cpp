#include <iostream>
#include "functions.hpp"

std::string name, title, house;
int house_number = 0;
bool end_story = false;
int story_choice;

void introduction() {

    std::cout << "============================================================\n";
    std::cout << "                    Welcome to Westeros!                    \n";
    std::cout << "============================================================\n";
    std::cout << "   This very short story puts you in George R.R. Martin's   \n";
    std::cout << "  fantasy world. Your choices determine your fate, and the  \n";
    std::cout << "  realm's. Try to unlock the best ending for your character.\n";
    std::cout << "\n";
    std::cout << "\n";

}

void run_story() {

    std::cout << "Create your character. First, what is your name?\n";
    std::cin >> name;
    std::cout << "\n";
    std::cout << "Next what is your title? Ser, Lady, Lord, etc. Choose any   \n";
    std::cout << "you would like. You be addressed as <title> " << name << ".\n";
    std::cin >> title;
    std::cout << "\n";
    std::cout << "As you wish, " << title << " " << name << ". Finally, which\n";
    std::cout << "noble house do you serve? Type 1 for Stark, 2 for Lannister,\n";
    std::cout << "or 3 for Greyjoy.\n";
    house_choice();
    std::cout << title << " " << name << ", of House " << house << ", now\n";
    std::cout << "begins your short adventure. Beware: the night is dark and \n";
    std::cout << "full of terrors.\n";
    std::cout << "\n";
    switch (house_number)
    {
    case 1:
        branch(1);
        break;
    case 2:
        branch(2);
        break;
    case 3:
        branch(3);
        break;
    default:
        break;
    }

}

void house_choice() {
    std::cin >> house_number;
    switch (house_number)
    {
    case 1:
        house == "Stark";
        break;
    case 2:
        house == "Lannister";
        break;
    case 3:
        house == "Greyjoy";
        break;
    default:
        std::cout << "Type 1 for Stark, 2 for Lannister, or 3 for Greyjoy.\n";
        std::cin >> house_number;
    }
    std::cout << "\n";
}

void stark0() {
    std::cout << title << " " << house << ", while resting in Winterfell with\n";
    std::cout << "your close family, a rider from Moat Cailin comes in the night.\n";
    std::cout << "\"Treachery! The Lannisters have amassed a host and are riding for\n";
    std::cout << "war up the Kingsroad. They have already taken the neck and will \n";
    std::cout << "be at Winterfell's gates on the fortnight!\"\n";
    std::cout << "\n"; 
    std::cout << "You will have to deal with that traitor, Walder Frey, later\n";
    std::cout << "for letting them through the Twins without a fight. But now you\n";
    std::cout << "must make a choice, as your banners are comfortably in their\n";
    std::cout << "holdfasts riding out this winter and the Lannisters will arrive\n";
    std::cout << "before most can make it to your aid.\n";

    std::cout << "Which decision will you make, my " << title << "?\n";
    std::cout << "choice1 or choice2?\n";

    std::cin >> story_choice;
    switch (story_choice)
    {
    case 1:
        branch(4);
        break;
    
    case 2:
        branch(5);
        break;
    default:
        std::cout << "Choose a valid number, 1 or 2.: ";
        std::cin >> story_choice;
        break;
    }
}

void battle_of_winterfell() {
    std::cout << "Battle of Winterfell text here.\n";
    end_story = true;   
}

void stark_betrayal() {
    std::cout << "Stark betrayal text here.\n";
    end_story = true;
}

void lannister0() {
    std::cout << title << " " << house << ", Lannister0 text here\n";

    std::cout << "Which decision will you make, my " << title << "?\n";
    std::cout << "choice1 or choice2?\n";

    std::cin >> story_choice;
    switch (story_choice)
    {
    case 1:
        branch(4);
        break;
    
    case 2:
        branch(6);
    
    default:
        std::cout << "Choose a valid number, 1 or 2.: ";
        std::cin >> story_choice;
        break;
    }
}

void crannogmen_attack() {
    std::cout << "Crannogmen attack text here.\n";
    end_story = true;
}

void greyjoy0() {
    std::cout << title << " " << house << ", Greyjoy0 text here\n";

    std::cout << "Which decision will you make, my " << title << "?\n";
    std::cout << "choice1 or choice2?\n";

    std::cin >> story_choice;
    switch (story_choice)
    {
    case 1:
        branch(4);
        break;
    
    case 2:
        branch(7);
    
    default:
        std::cout << "Choose a valid number, 1 or 2.: ";
        std::cin >> story_choice;
        break;
    }
}

void bolton_flaying() {
    std::cout << "Bolton flaying text here.\n";
    end_story = true;
}

void story() {
    while (!end_story) {
        run_story();    
    }
}

void branch(int choice) {
    switch (choice)
    {
    case 1:
        stark0();
        break;
    case 2:
        lannister0();
        break;
    case 3:
        greyjoy0();
        break;
    case 4:
        battle_of_winterfell();
        break;
    case 5:
        stark_betrayal();
        break;
    case 6:
        crannogmen_attack();
        break;
    case 7:
        bolton_flaying();
        break;
    default:
        break;
    }
}

void ending() {
    std::cout << "Come back for the sequel in 1 to 99 years!\n";
    std::cout << "Thanks for playing!\n";
}