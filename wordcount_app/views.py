from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def check_punc(word):
    punc_set = {',', '.', '?', '!'}
    return word[-1] in punc_set

def word_count(word_dict, word):
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

def result(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dict = {}
    for word in word_list:
        if check_punc(word):
            word_count(word_dict, word[:-1])
        else:
            word_count(word_dict, word)
    return render(request, 'wordcount/result.html', {'fulltext': full_text, 'total': sum(word_dict.values()), 'dictionary': sorted(word_dict.items())})