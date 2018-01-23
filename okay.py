def lyrics_frequency(lyrics):
    my_dict = {}
    #Going through the lyrics
    for word in lyrics:
#if the word is in the dictionary then add it by one
        if word in my_dict:
            my_dict[word]+=1
#else take it as 1
        else:
            my_dict[word]=1
# return the value of my_dict
    return my_dict
lyric = """Escaping nights without you with shadows on the wall My mind is running wild tryin' hard not to fall You told me that you love me but say I'm just a friend My heart is broken up into pieces Cause I know Ill never free my soul
Its trapped between true love and being alone
When my eyes are closed the greatest story told
I woke and my dreams are shattered here on the floor
Why oh why tell me why not me
Why oh why we were meant to be
Baby I know I could be all you need
Why oh why oh why
I wanna love you
If you only knew how much I love you
So why not me
The day after tomorrow I'll still be around
To catch you when you fall and ever let you down
You say that we're forever our love will never end
I've tried to come up but it's drowning me to know"""
why_not_me=lyric.split()
#print(why_not_me),
print(lyrics_frequency(why_not_me))
print(why_not_me.count(str(input('enter the word to find the number of occurance (warning: its case sensitive)'))))

