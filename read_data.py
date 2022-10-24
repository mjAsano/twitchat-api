import pandas as pd

class ReadData():
        
    channel_id = ""
    video_id = ""
    match_word = ""
    
    def get_chat_data(self, channel_id, video_id, match_word):
        
        self.channel_id = channel_id
        self.video_id = video_id
        self.match_word = match_word
        
        df = pd.read_csv("./" + self.channel_id + '/' + self.video_id + '.csv', error_bad_lines=False)
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
        
        print(data)  
        data.to_csv('./output/test_result.csv')
            
        return data

