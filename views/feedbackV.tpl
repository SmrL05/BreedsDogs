% rebase('layout.tpl', title=title, year=year, error = error, errorCheck=errorCheck)
<img src="/static/image/picFeedback.jpg" height = 640 margin = 0px/>
<div class="row">
    <div class="col-md-12 gap-3 border-10 margin-top-5" id="block_background" style="height: 400px">
        
           <div class="jumbotron  text-center" id="block_background" style="height: 240px" >
                <h2  class="h">Add your feedback</h2>
                 <font color="white" class="lead">You can leave your email and phone number to receive notifications about new site updates, as well as receive additional points from our partners for your feedback.</font>
                  <p class="erorrtext_" style="color: #b94a48;">{{error}}</p>
            </div>
           <form action="/feedback" method="post">
               <div class="col-md-3 col-md-offset-2">
                    <p><input type="text" class="input" size="70" name="NICKNAME" value="{{errorCheck[0]}}" placeholder="Your nickname"></input></p>
                    <p><input type="text" class="input" size="50" name="EMAIL" value="{{errorCheck[1]}}" placeholder="Your email"></input></p>
                    <p><input type="text" class="input" size="50" name="PHONE" value="{{errorCheck[2]}}" placeholder="Your phone"></input></p>
               </div>
               <div class="col-md-3 col-md-offset-0">
                    <textarea  style="resize : none;" class="input" rows="5" cols="80" name="FEEDBACKTEXT" placeholder="Feedback text">{{errorCheck[3]}}</textarea>
                    
               </div>
                    <button class="shine-button">Send</p></button>
            </form>
    </div>
</div>


%import json
%dictionary = {}
%with open('feedbacks.txt') as json_file:
    %dictionary = json.load(json_file)
%for i in reversed(dictionary):
    <div class="row">
        <div class="col-md-12 gap-3 border-10 margin-top-0" id="block_background" style="height: 300px">
           <hr />
           <div class="col-md-3 col-md-offset-0">
                <img src="/static/image/icon_user.png" height=300/>
           </div>
           <div class="col-md-8 col-md-offset-0">
                <h2 class="h">{{dictionary[i]['nickname']}}</h2>
                <p style="color: #ffffff;font-size: 26px;">{{dictionary[i]['feedbacktexts']}}</p>
                <p class="lead" style="color: #4a4a4a; justify-content: right;">{{dictionary[i]['dates']}} {{dictionary[i]['times']}}</p>
           </div>
        </div>
    </div>


    