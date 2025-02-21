function locomotive() {
  gsap.registerPlugin(ScrollTrigger);

  const locoScroll = new LocomotiveScroll({
    el: document.querySelector("#main"),
    smooth: true ,
  });
  locoScroll.on("scroll", ScrollTrigger.update);

  ScrollTrigger.scrollerProxy("#main", {
    scrollTop(value) {
      return arguments.length
        ? locoScroll.scrollTo(value, 0, 0)
        : locoScroll.scroll.instance.scroll.y;
    },

    getBoundingClientRect() {
      return {
        top: 0,
        left: 0,
        width: window.innerWidth,
        height: window.innerHeight,
      };
    },

    pinType: document.querySelector("#main").style.transform
      ? "transform"
      : "fixed",
  });
  ScrollTrigger.addEventListener("refresh", () => locoScroll.update());
  ScrollTrigger.refresh();
}
locomotive();


const canvas = document.querySelector("canvas");
const context = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;


window.addEventListener("resize", function () {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  render();
});

function files(index) {
  var data = `
     ./static/images/male0001.png
     ./static/images/male0002.png
     ./static/images/male0003.png
     ./static/images/male0004.png
     ./static/images/male0005.png
     ./static/images/male0006.png
     ./static/images/male0007.png
     ./static/images/male0008.png
     ./static/images/male0009.png
     ./static/images/male0010.png
     ./static/images/male0011.png
     ./static/images/male0012.png
     ./static/images/male0013.png
     ./static/images/male0014.png
     ./static/images/male0015.png
     ./static/images/male0016.png
     ./static/images/male0017.png
     ./static/images/male0018.png
     ./static/images/male0019.png
     ./static/images/male0020.png
     ./static/images/male0021.png
     ./static/images/male0022.png
     ./static/images/male0023.png
     ./static/images/male0024.png
     ./static/images/male0025.png
     ./static/images/male0026.png
     ./static/images/male0027.png
     ./static/images/male0028.png
     ./static/images/male0029.png
     ./static/images/male0030.png
     ./static/images/male0031.png
     ./static/images/male0032.png
     ./static/images/male0033.png
     ./static/images/male0034.png
     ./static/images/male0035.png
     ./static/images/male0036.png
     ./static/images/male0037.png
     ./static/images/male0038.png
     ./static/images/male0039.png
     ./static/images/male0040.png
     ./static/images/male0041.png
     ./static/images/male0042.png
     ./static/images/male0043.png
     ./static/images/male0044.png
     ./static/images/male0045.png
     ./static/images/male0046.png
     ./static/images/male0047.png
     ./static/images/male0048.png
     ./static/images/male0049.png
     ./static/images/male0050.png
     ./static/images/male0051.png
     ./static/images/male0052.png
     ./static/images/male0053.png
     ./static/images/male0054.png
     ./static/images/male0055.png
     ./static/images/male0056.png
     ./static/images/male0057.png
     ./static/images/male0058.png
     ./static/images/male0059.png
     ./static/images/male0060.png
     ./static/images/male0061.png
     ./static/images/male0062.png
     ./static/images/male0063.png
     ./static/images/male0064.png
     ./static/images/male0065.png
     ./static/images/male0066.png
     ./static/images/male0067.png
     ./static/images/male0068.png
     ./static/images/male0069.png
     ./static/images/male0070.png
     ./static/images/male0071.png
     ./static/images/male0072.png
     ./static/images/male0073.png
     ./static/images/male0074.png
     ./static/images/male0075.png
     ./static/images/male0076.png
     ./static/images/male0077.png
     ./static/images/male0078.png
     ./static/images/male0079.png
     ./static/images/male0080.png
     ./static/images/male0081.png
     ./static/images/male0082.png
     ./static/images/male0083.png
     ./static/images/male0084.png
     ./static/images/male0085.png
     ./static/images/male0086.png
     ./static/images/male0087.png
     ./static/images/male0088.png
     ./static/images/male0089.png
     ./static/images/male0090.png
     ./static/images/male0091.png
     ./static/images/male0092.png
     ./static/images/male0093.png
     ./static/images/male0094.png
     ./static/images/male0095.png
     ./static/images/male0096.png
     ./static/images/male0097.png
     ./static/images/male0098.png
     ./static/images/male0099.png
     ./static/images/male0100.png
     ./static/images/male0101.png
     ./static/images/male0102.png
     ./static/images/male0103.png
     ./static/images/male0104.png
     ./static/images/male0105.png
     ./static/images/male0106.png
     ./static/images/male0107.png
     ./static/images/male0108.png
     ./static/images/male0109.png
     ./static/images/male0110.png
     ./static/images/male0111.png
     ./static/images/male0112.png
     ./static/images/male0113.png
     ./static/images/male0114.png
     ./static/images/male0115.png
     ./static/images/male0116.png
     ./static/images/male0117.png
     ./static/images/male0118.png
     ./static/images/male0119.png
     ./static/images/male0120.png
     ./static/images/male0121.png
     ./static/images/male0122.png
     ./static/images/male0123.png
     ./static/images/male0124.png
     ./static/images/male0125.png
     ./static/images/male0126.png
     ./static/images/male0127.png
     ./static/images/male0128.png
     ./static/images/male0129.png
     ./static/images/male0130.png
     ./static/images/male0131.png
     ./static/images/male0132.png
     ./static/images/male0133.png
     ./static/images/male0134.png
     ./static/images/male0135.png
     ./static/images/male0136.png
     ./static/images/male0137.png
     ./static/images/male0138.png
     ./static/images/male0139.png
     ./static/images/male0140.png
     ./static/images/male0141.png
     ./static/images/male0142.png
     ./static/images/male0143.png
     ./static/images/male0144.png
     ./static/images/male0145.png
     ./static/images/male0146.png
     ./static/images/male0147.png
     ./static/images/male0148.png
     ./static/images/male0149.png
     ./static/images/male0150.png
     ./static/images/male0151.png
     ./static/images/male0152.png
     ./static/images/male0153.png
     ./static/images/male0154.png
     ./static/images/male0155.png
     ./static/images/male0156.png
     ./static/images/male0157.png
     ./static/images/male0158.png
     ./static/images/male0159.png
     ./static/images/male0160.png
     ./static/images/male0161.png
     ./static/images/male0162.png
     ./static/images/male0163.png
     ./static/images/male0164.png
     ./static/images/male0165.png
     ./static/images/male0166.png
     ./static/images/male0167.png
     ./static/images/male0168.png
     ./static/images/male0169.png
     ./static/images/male0170.png
     ./static/images/male0171.png
     ./static/images/male0172.png
     ./static/images/male0173.png
     ./static/images/male0174.png
     ./static/images/male0175.png
     ./static/images/male0176.png
     ./static/images/male0177.png
     ./static/images/male0178.png
     ./static/images/male0179.png
     ./static/images/male0180.png
     ./static/images/male0181.png
     ./static/images/male0182.png
     ./static/images/male0183.png
     ./static/images/male0184.png
     ./static/images/male0185.png
     ./static/images/male0186.png
     ./static/images/male0187.png
     ./static/images/male0188.png
     ./static/images/male0189.png
     ./static/images/male0190.png
     ./static/images/male0191.png
     ./static/images/male0192.png
     ./static/images/male0193.png
     ./static/images/male0194.png
     ./static/images/male0195.png
     ./static/images/male0196.png
     ./static/images/male0197.png
     ./static/images/male0198.png
     ./static/images/male0199.png
     ./static/images/male0200.png
     ./static/images/male0201.png
     ./static/images/male0202.png
     ./static/images/male0203.png
     ./static/images/male0204.png
     ./static/images/male0205.png
     ./static/images/male0206.png
     ./static/images/male0207.png
     ./static/images/male0208.png
     ./static/images/male0209.png
     ./static/images/male0210.png
     ./static/images/male0211.png
     ./static/images/male0212.png
     ./static/images/male0213.png
     ./static/images/male0214.png
     ./static/images/male0215.png
     ./static/images/male0216.png
     ./static/images/male0217.png
     ./static/images/male0218.png
     ./static/images/male0219.png
     ./static/images/male0220.png
     ./static/images/male0221.png
     ./static/images/male0222.png
     ./static/images/male0223.png
     ./static/images/male0224.png
     ./static/images/male0225.png
     ./static/images/male0226.png
     ./static/images/male0227.png
     ./static/images/male0228.png
     ./static/images/male0229.png
     ./static/images/male0230.png
     ./static/images/male0231.png
     ./static/images/male0232.png
     ./static/images/male0233.png
     ./static/images/male0234.png
     ./static/images/male0235.png
     ./static/images/male0236.png
     ./static/images/male0237.png
     ./static/images/male0238.png
     ./static/images/male0239.png
     ./static/images/male0240.png
     ./static/images/male0241.png
     ./static/images/male0242.png
     ./static/images/male0243.png
     ./static/images/male0244.png
     ./static/images/male0245.png
     ./static/images/male0246.png
     ./static/images/male0247.png
     ./static/images/male0248.png
     ./static/images/male0249.png
     ./static/images/male0250.png
     ./static/images/male0251.png
     ./static/images/male0252.png
     ./static/images/male0253.png
     ./static/images/male0254.png
     ./static/images/male0255.png
     ./static/images/male0256.png
     ./static/images/male0257.png
     ./static/images/male0258.png
     ./static/images/male0259.png
     ./static/images/male0260.png
     ./static/images/male0261.png
     ./static/images/male0262.png
     ./static/images/male0263.png
     ./static/images/male0264.png
     ./static/images/male0265.png
     ./static/images/male0266.png
     ./static/images/male0267.png
     ./static/images/male0268.png
     ./static/images/male0269.png
     ./static/images/male0270.png
     ./static/images/male0271.png
     ./static/images/male0272.png
     ./static/images/male0273.png
     ./static/images/male0274.png
     ./static/images/male0275.png
     ./static/images/male0276.png
     ./static/images/male0277.png
     ./static/images/male0278.png
     ./static/images/male0279.png
     ./static/images/male0280.png
     ./static/images/male0281.png
     ./static/images/male0282.png
     ./static/images/male0283.png
     ./static/images/male0284.png
     ./static/images/male0285.png
     ./static/images/male0286.png
     ./static/images/male0287.png
     ./static/images/male0288.png
     ./static/images/male0289.png
     ./static/images/male0290.png
     ./static/images/male0291.png
     ./static/images/male0292.png
     ./static/images/male0293.png
     ./static/images/male0294.png
     ./static/images/male0295.png
     ./static/images/male0296.png
     ./static/images/male0297.png
     ./static/images/male0298.png
     ./static/images/male0299.png
     ./static/images/male0300.png
 `;
  return data.split("\n")[index];
}

const frameCount = 300;

const images = [];
const imageSeq = {
  frame: 1,
};

for (let i = 0; i < frameCount; i++) {
  const img = new Image();
  img.src = files(i);
  images.push(img);
}

gsap.to(imageSeq, {
  frame: frameCount - 1,
  snap: "frame",
  ease: `none`,
  scrollTrigger: {
    scrub: 0.15,
    trigger: `#page>canvas`,
    start: `top top`,
    end: `600% top`,
    scroller: `#main`,
  },
  onUpdate: render,
});

images[1].onload = render;

function render() {
  scaleImage(images[imageSeq.frame], context);
}

function scaleImage(img, ctx) {
  var canvas = ctx.canvas;
  var hRatio = canvas.width / img.width;
  var vRatio = canvas.height / img.height;
  var ratio = Math.max(hRatio, vRatio);
  var centerShift_x = (canvas.width - img.width * ratio) / 2;
  var centerShift_y = (canvas.height - img.height * ratio) / 2;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(
    img,
    0,
    0,
    img.width,
    img.height,
    centerShift_x,
    centerShift_y,
    img.width * ratio,
    img.height * ratio
  );
}
ScrollTrigger.create({
  trigger: "#page>canvas",
  pin: true,
  // markers:true,
  scroller: `#main`,
  start: `top top`,
  end: `600% top`,
});



gsap.to("#page1",{
  scrollTrigger:{
    trigger:`#page1`,
    start:`top top`,
    end:`bottom top`,
    pin:true,
    scroller:`#main`
  }
})
gsap.to("#page2",{
  scrollTrigger:{
    trigger:`#page2`,
    start:`top top`,
    end:`bottom top`,
    pin:true,
    scroller:`#main`
  }
})
gsap.to("#page3",{
  scrollTrigger:{
    trigger:`#page3`,
    start:`top top`,
    end:`bottom top`,
    pin:true,
    scroller:`#main`
  }
})