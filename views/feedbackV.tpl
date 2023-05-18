% rebase('layout.tpl', title=title, year=year)
<img src="/static/image/picFeedback.jpg" height = 640 margin = 0px/>
 <div class="row">
        <div class="col-md-12 gap-3 border-10 margin-top-0" id="block_background" style="height: 300px">
           <div class="jumbotron  text-center margin-5" id="block_background" style="height: 40px" >
                <h2  class="h">Add your feedback</h2>
            </div>
           <form action="/feedback" method="post">
               <div class="col-md-3 col-md-offset-0">
                    <p><input type="text" class="input" size="50" name="NICKNAME" placeholder="Your nickname"></p>
                    <p><input type="text" class="input" size="50" name="EMAIL" placeholder="Your email"></p>
                    <p><input type="text" class="input" size="50" name="DATE_" placeholder="Date now"></p>
               </div>
               <div class="col-md-3 col-md-offset-0">
                    <p><textarea  style="resize : none;" class="input" rows="5" cols="80" name="FEEDBACKTEXT" placeholder="Feedback text"></textarea></p> 
               </div>
               <p><a class="shine-button">Send</a></p>
            </form>
        </div>
        
 </div>

%a = 5
%while a>0:
    <div class="row">
        <div class="col-md-12 gap-3 border-10 margin-top-0" id="block_background" style="height: 300px">
           <hr />
           <div class="col-md-3 col-md-offset-0">
                <img src="/static/image/pug.jpeg" height=200/>
           </div>
           <div class="col-md-3 col-md-offset-0">
                <h2 class="h">nickname</h2>
                <p style="color: #ffffff;">text feedback</p>
                <p class="lead" style="color: #4a4a4a; justify-content: right;">time</p>
           </div>
        </div>
    </div>
    %a-=1
