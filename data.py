import pandas as pd
import os

class GetData():

    loc_out = "./channels/"
    channel_id = ""
    video_id = ""
    match_word = ""

    def __init__(self, loc_out):
        self.loc_out= loc_out
    
    def get_video_list(self, channel_id):    
        self.channel_id = channel_id
        channels = os.listdir('channels/' + self.channel_id)
        print(channels)
        return channels
        
    
    def get_chat_data(self, channel_id, video_id, match_word):
        
        self.channel_id = channel_id
        self.video_id = video_id
        self.match_word = match_word

        
        df = pd.read_csv(self.loc_out + self.channel_id + '/' + self.video_id + '.csv', error_bad_lines=False)
        df.columns = ['time','id','msg']

        stop_word = match_word
        data = df[df['msg'].str.contains(match_word)]
        print(stop_word)
        data['link'] = data['time']
        data = data.reset_index(drop=True)

        cur_time = []
        timeline = "" 
        for i in range(0, len(data['link'])):
            cur_time = data['link'][i].split(':')
            timeline = cur_time[0]+'h'+cur_time[1]+'m'+cur_time[2]+'s'
            data['link'][i] = ("https://www.twitch.tv/videos/"+self.video_id+"?t=%s" % (timeline))
            #data['time'][i] = timeline
        #print(data)  
        #data.to_csv('./output/test_result.csv')    

        return data

