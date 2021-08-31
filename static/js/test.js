const target_url = ["ur11", "ur12", "url3"];

// 다운로드에 약 1초가 걸리는 비동기 함수라고 가정
function async_download(url) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(url);
            resolve();
        }, 1000);
    });
}

async function parallel(array) {
    const promises = array.map((url) => async_download(url));
    await Promise.all(promises);
    console.log("all done :)");
}

parallel(target_url);