% rebase('layout.tpl', title=title, year=year, titleArticle = titleArticle, article = article, urlArticle = urlArticle, name = name, email = email, phone = phone, state = state, error=error)
<img src="/static/image/picArticle.jpg" height = 640 margin = 0px/>

%if (state == 1):
    <script>
        function scrollToBottom() {
            window.scrollTo(0, 640);
        }
        window.onload = scrollToBottom;
    </script>
%end

<div class="row">
    <div class="col-md-12 gap-3 border-10 margin-top-0" id="block_background" style="height: 430px">
        <div class="jumbotron  text-center margin-5" id="block_background" style="height: 40px" >
            <h2 class="h p-20">Add your article</h2>
        </div> 
        <form action="/article" method="post">
            <div class="row p-top-left-20">
                <div class="col-md-3 col-md-offset-0 border-10" style="margin: 2px 45px 2px 230px;">
                    <p><textarea style="resize: none;" class="input" rows="2" cols="80" name="TITLE_ARTICLE" placeholder="The title of your article">{{titleArticle}}</textarea></p>
                    <p><textarea style="resize: none;" class="input" rows="8" cols="80" name="ARTICLE" placeholder="Abstract for your article">{{article}}</textarea></p> 
                </div>   
                <div class="col-md-3 col-md-offset-0 border-10" style="margin: 2px 180px 2px 45px;">
                    <p><textarea style="resize: none;" class="input" rows="2" cols="80" name="URL_ARTICLE" placeholder="Link to your article">{{urlArticle}}</textarea></p>
                    <p><textarea style="resize: none;" class="input" rows="1" cols="80" name="NAME_AUTHOR" placeholder="Name of author">{{name}}</textarea></p>
                    <p><textarea style="resize: none;" class="input" rows="1" cols="80" name="EMAIL_AUTHOR" placeholder="Email of author">{{email}}</textarea></p>
                    <p><textarea style="resize: none;" pattern="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$" class="input" rows="1" cols="80" name="PHONE_AUTHOR" placeholder="Phone of author">{{phone}}</textarea></p>
                    <p><input type="submit" class="shine-button" value="Add"></p>
                </div>                   
            </div>   
            <div class="col-md-12 col-md-offset-0" style="text-align: center;">
                <h3 class = "erorrtext_ flex-center-col"><b>{{error}}</b></h3>
            </div>
        </form>
    </div>   
 </div>

%import json
%dictionary = {}
% with open('articles.txt') as json_file:
    %dictionary = json.load(json_file)
%for i in reversed(dictionary):
    <div class="row">
        <div class="col-md-12 gap-3 col-md-offset-0 border-10 margin-top-0" id="block_background" style="height: 300px">
           <hr />
           <div class="col-md-4 col-md-offset-0">
                <img src="/static/image/avatar.jpg" height=200/>
           </div>
           <div class="col-md-8 col-md-offset-0">
                <h2 class="h">{{dictionary[i]['titleArticle']}}</h2>
                <h3 class="h">Avtor: {{dictionary[i]['name']}}, Date of publication: {{dictionary[i]['date']}}</h3>
                <p style="color: #ffffff;">{{dictionary[i]['article']}}</p>
                <p><a class="shine-button" href="{{dictionary[i]['urlArticle']}}">Learn more</a></p>
           </div>
        </div>
    </div>