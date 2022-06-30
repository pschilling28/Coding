# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

# finds word in body and replaces it with <REDACTED>, returns body with all instances redacted
def censor(word_or_phrase, body):
    body = body.replace(word_or_phrase, " <REDACTED> ")
    return body

# returns new list from list of words that include versions of words with spaces and capitalized first letters to help prevent censoring chunks of words in a string (i.e. "hers" in "researchers")
def scrub_list(list_of_words_or_phrases):
    scrubbed_list = []
    for item in list_of_words_or_phrases:
        scrubbed_list.append(item + " ")
        scrubbed_list.append(" " + item)
        scrubbed_list.append(item[0].upper() + item[1:])
    return scrubbed_list

# sorts scrubbed list (see scrub_list() comments) by descending word length to prevent small words that are part of larger words from being redacted first (leaving part of a larger word, instead of redacting the full larger word), then finds list of words in body and replaces scrubbed versions of each in body with <REDACTED>
def censor_from_list(list_of_words_or_phrases, body):
    list_of_words_or_phrases = scrub_list(sorted(list_of_words_or_phrases, key=len, reverse=True))
    for word_or_phrase in list_of_words_or_phrases:
        body = body.replace(word_or_phrase, " <REDACTED> ")
    return body

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# list to help deal with punctuation
punctuation_list = [".", "!", ",", ":", "?"]

# sorts scrubbed list for reasons commented above, checks if any word on the list collectively occurs more than twice and, if so, redacts all of the words from the list from the body
def censor_from_list_if_greater_than_2_x(list_of_words_or_phrases, body):
    list_of_words_or_phrases = scrub_list(sorted(list_of_words_or_phrases, key=len, reverse=True))
    word_from_list_count = 0
    for word_or_phrase in list_of_words_or_phrases:
        if word_or_phrase in body:
            word_from_list_count += 1
    if word_from_list_count > 2:
        for word_or_phrase in list_of_words_or_phrases:
            body = body.replace(word_or_phrase, " <REDACTED> ")            
    return body 

# splits body into lines and words, finds <REDACTED> in words list and, if the preceeding or following word is not punctuation, changes it to <REDACTED> (used a space on either end to prevent overwriting itself in the for loop), and rebuilds new email body, adding spaces after words and line breaks after lines
def censor_before_and_after_redactions(body):
    line_list = body.split("\n")
    word_list = []
    new_body = ""
    for i in range(len(line_list) - 1):
        word_list.append(line_list[i].split())
    for i in range(len(word_list) - 1):
        for j in range(len(word_list[i]) - 1):
            if word_list[i][j] == "<REDACTED>":
                if word_list[i][j - 1] not in punctuation_list:
                    word_list[i][j - 1] = "<REDACTED> "
                if word_list[i][j + 1] not in punctuation_list:
                    word_list[i][j + 1] = " <REDACTED>"
    for line in word_list:
        for word in line:
            new_body += word + " "
        new_body += "\n"

    return new_body

# test functions
test1 = censor("learning algorithms", email_one)
#print(test1)

test2 = censor_from_list(proprietary_terms, email_two)
#print(test2)

test3 = censor_from_list(proprietary_terms, censor_from_list_if_greater_than_2_x(negative_words, email_three))
#print(test3)

test4 = censor_before_and_after_redactions(censor_from_list(proprietary_terms, censor_from_list_if_greater_than_2_x(negative_words, email_four)))
#print(test4)