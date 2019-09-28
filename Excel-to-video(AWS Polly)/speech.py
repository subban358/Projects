import boto3
poly = boto3.client('polly')

def play(text):
    response = poly.synthesize_speech(Text=text,VoiceId='Joanna',OutputFormat='mp3')
    body = response['AudioStream'].read()
    file_name = 'voice.mp3'
    with open(file_name,'wb') as file:
        file.write(body)
        file.close()

if __name__ == '__main__':
    file1 = open('n.txt','r+')
    play(file1.read())
   #play("hi how are you")