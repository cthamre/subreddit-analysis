# subreddit-analysis
I used these two scripts to extract and perform basic analysis on the data I used for my dissertation project.

subreddit_extraction uses PRAW and requires that you set up a reddit account with the reddit API. It contains the function redditsearch, which requires you to define the name of the subreddit that will be accessed as well as your reddit API credentials: Your client id, client secret, username, password, and user agent. Its output is a text file of tab-separated columns. Each row contains the username, date (in UNIX epoch), and text of a Reddit post title, post body, or comment. It also generates three other files containing each of these individually in a single column. It does not perform any kind of cleaning on the text data, although it does convert line breaks within a post or comment to spaces in order to display them on a single line.

lex_data is designed to extract lexical data from a series of corpora. When you run it, your directory must contain a text file called "variables.txt", containing rows that consist of two lexical variants separated by a comma (e.g. "beside,next to"), as well as a folder called "Corpora", containing a series of text files which you wish to analyze. The script produces four files: wordcounts.txt, which contains the raw count of each lexical variant in each corpus; varpermils.txt, which contains the frequency per million of each lexical variant in each corpus; ratios.txt, which contains the ratio of the frequency per million values of each pair of lexical variants in each corpus; and corpuswordcounts.txt, which contains the total word count of each corpus.

I recommend [this tutorial](https://www.youtube.com/watch?v=NRgfgtzIhBQ&ab_channel=sentdex) to get started with PRAW.

## License
[MIT](https://choosealicense.com/licenses/mit/)
