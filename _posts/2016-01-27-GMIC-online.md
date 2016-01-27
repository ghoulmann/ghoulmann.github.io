# There's G'MIC

Last Summer, I spent a lot of time tinkering with Google's Symptom, artificial neural network's so called _DeepDream_ images. My goal was create a script that scraped images from a given tumblr, process them uniformly with Imagemagick, and then pass them through a couple of deepdream filters. I had found a recipe I liked, and enjoyed seeing it work with consistent success for any set of images I scraped.

[I used scraped images in a tmp directory to ensure the recipe worked for a wide variety of circumstances.]

Today, however, I learned a bit about G'MIC, and it looks like I could have done what I accomplished with ImageMagick with G'MIC instead. And it would have taken a bit less scripting. Note, I haven't fully explored scripting with G'MIC yet.

Things I Should Have Known:

1. G'MIC is not just a gimmick in the GIMP. It is a powerful scripting tool for image processing.

1. G'MIC has a [Web-based, online image editor](https://gmicol.greyc.fr/) that looks quite polished and does a great job of introducing visitors to G'MIC's reality tunnel.

For a lot more background on G'MIC, visit [this](http://www.dpreview.com/forums/post/53654570) post.

From here I yatter on about G'MIC online.

## [G'MIC online](https://gmicol.greyc.fr/)

My instinct as film photographer, most interested in concert shots, is to try to reproduce with a digital camera the texture of a film shot: particularly, the texture of TMAX3200, the film stock I relied on most. There was a Photoshop addon that helped with this...by alienskin I think. When I moved to Ubuntu and The Gimp for processing photos manually, I had to find a combination of filters that gave me a similar effect.

Using G'MIC online, I can manipulate images stored locally. Instead of working with a shot of my own, I've chosen this shot:

<img src="http://www.pop-kultur.berlin/wp-content/uploads/2015/04/HO99O9-live.jpg">

<caption>Before applying filters</caption>


The subject is the New Jersey band Ho99o9 performing live. A lot of envy for this shot, which is far from how I might have captured the moment. My hope is to keep energy of this moment but to mimic the texture of my preferred film stock. I also want to subtly increase contrast: the image has a grey tone to it; there's not the contrast I like: but there is detail. Fantastic detail: Look at the singers jeans, or the top of the head of the man holding up the singer's leg and back. I don't want to lose that detail.

1. Start from a shot on local storage

2. Navigate to https://gmicol.greyc.fr/

3. On the left side of the page, at the bottom of the "Preview" pane, click _Open file..._, and navigate to the photo you'd like to manipulate.
4. The center panel offers over 300 filters, pretty well categorized. I'm simply going to choose _Film Emulation_, choose _B&W Films_, and then choose the preset I prefer: TMAX3200. I elect not to manually adjust the filter.

5. When I'm happy with the preview, I click _Render Full Image_. I now have to choices, _Download_ and _Set as New Input_. I want to fully inspect the new image, so I choose _Download_. Here's what I find:

![](http://rikgoldman.ghost.io/content/images/2016/01/GMICImage.jpg)

<caption>Filter applied</caption>

When I inspect the image, I look first at whether the very darkest parts of the image have detail: the stage, for example. I'm happy with the stage, the parts of the floor I can make out, and the wall barely visibly at the left-center edge.

So I turn to highlights, making sure nothing is completely overblown: I'm looking for detail in the highlights. I see the man in the center's jeans...comparing the before/after images, I'm really impressed, but provisionally: the contrast has increased, rather strongly, but there's still detail in the two hot spots: the singer's jeans and the man's head.

Also, the artifacts are present: artifacts reminiscent of photos shot on TMAX3200. Perfect there.

I'm not wholly satisfied with the result. I feel certain after this first attempt, though, that if I adjust curves ahead of time, and manually override the filter presets for this effect, I'll have accomplished the trifling little effect that I'm after.

I'm confident now that I can go out, shoot a performance in a dark club with my Nikon D3000, and run a bash script that relies on G'MAC to produce shots reminiscent of what's in my portfolio.
![](http://rikgoldman.ghost.io/content/images/2016/01/GMICImage2-1.jpg)

After some tweaking, I can see muscle tone in the highlights, but TMAX filter works as I wanted it to.

If a silly person asked if there's anything Windows could do that I miss in Ubuntu...that last trifle, a TMAX3200 filter, is no longer on the list.

The list is empty. There is nothing to be nostalgic about when it comes to my production environment.
