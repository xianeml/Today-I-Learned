# Async, AJAX, API

# The call stack

스택은 자료구조. **`LIFO` last in first out**

호출스택은 자바스크립트가 많은 함수콜에서 어디에있는지 트래킹하기 위한것.

스크립트에서 함수 호출하면 인터프리터가 함수를 콜 스택에 추가함. 호출된 함수들은 호출스택에 추가되고 실행된다. 현재 함수리턴하고 끝나면 스택에서 사라짐 푸시 팝팝

이거 알고리즘할때 공부햇음

[latentflip.com/loupe](http://latentflip.com/loupe) 이 사이트에서 코드작성하면 호출스택 비쥬얼 보여줌

```java
const multiply = (x, y) => x * y;

const square = x => multiply(x, x);

const isRightTriangle = (a, b, c) => (
	square(a) + square(b) === square(c)
)
```

저 마지막 애는 스퀘어 함수를 3번 호출한다. 스퀘어 함수는 또 multi함수 호출

함수가 각각 호출되면서 이렇게 호출스택이 쌓였지. 지금 저 맨밑 트라이앵글은 답을 기다리고있다. 맨위에껀 이제 더 호출할거없고 실행끝났으니까 스택에서 사라진다. 그다음꺼도 사라지고 마지막꺼도 9라는 결과를 반환하고 사라짐. 이렇게 스택이 총 3번 쌓여졌다가 사라진다.

콘솔 소스탭에서 내 스크립트파일 선택하고

break point 클릭하면 새로고침할때 그 라인부터 코드실행 정지됨

콜스택을 볼 수 있음

포인트 걸어서 어디가 문제였는지 따라갈수있다

# JS is single threaded

자바스크립트 프로세스 at any given point 에서 작동하는 하나가 있다

멀티 ㄴㄴ 한번에 한 라인씩 처리된다

```java
console.log("sending request to server!");
setTimeout(() => {
  console.log("here is your data!"); //3초 후
}, 3000);
console.log("im at the end of the file!");
```

settimeout 3초 머물러줘~ 얘는 웹 API function

3초 세는건 브라우저가 해준다. 걔는 c++같은 다른 언어로 만들어짐

브라우저 수행 끝나면 끝났다고 자바스크립트에게 알려줌

# Callback Hell:(

```
setTimeout(() => {
    document.body.style.backgroundColor = 'red';
    setTimeout(() => {
        document.body.style.backgroundColor = 'orange';
        setTimeout(() => {
            document.body.style.backgroundColor = 'yellow';
            setTimeout(() => {
                document.body.style.backgroundColor = 'green';
                setTimeout(() => {
                    document.body.style.backgroundColor = 'blue';
                }, 1000)
            }, 1000)
        }, 1000)
    }, 1000)
}, 1000)
```

레드 → 오렌지 → 옐로우

```
const delayedColorChange = (newColor, delay, doNext) => {
    setTimeout(() => {
        document.body.style.backgroundColor = newColor;
        doNext && doNext();
    }, delay)
}
```

```
// STILL A LOT OF NESTING!!!
delayedColorChange('red', 1000, () => {
    delayedColorChange('orange', 1000, () => {
        delayedColorChange('yellow', 1000, () => {
            delayedColorChange('green', 1000, () => {
                delayedColorChange('blue', 1000, () => {

                })
            })
        })
    })
});
```

위와같은 경우엔 우리가 몇초 지연될지 직접 정해주는거잖아

근데 몇초지연되는지 모르는경우가 있어

예를들어 fake code:

내가 무비 데이터베이스로 작업한다하자

검색과 저장 두가지 작업을 거칠거야.

```java
searchMoviesAPI('amadeus', ()=>{
    saveToMyDB(movies, () => {
        //if it works, run this:
    }, () => {
        //if it doesn't work, run this:
    })
}, () => {
	//if API is down, or request failed
})
```

아마데우스를 찾는다. 아주많은 시간이 걸릴거야. 얼마나 걸릴지 몰라

그래서 그 디비가 존재하지 않을 경우의 함수랑 성공했을때 함수를 만들어주는거야

아마데우스를 찾으면 내 디비에 저장해줘 (그 무비를). 이게 첫번째 작업에 의존하고있어서 중첩된거지

저장할때도 시간이 걸린다. 잘 되거나 안되거나. 성공과 실패의 경우 실행할 콜백을 적어준다.

지금 작업과정 2개에 성공과 실패 콜백이 들어갔지. 작업이 늘어남에 따라 앞으로 이런 if else 과정이 많아질거야. 그럼 당연히 어글리 콜백 헬에 빠질수있어

중첩함수가 계속 콜백으로 이어지는거 개선 → 프로미스/

첫번째 요청 성공하면 두번째 요청만들어서 성공실패 만들고 거기서 성공하면 또 그안에서 새로운 요청 만들고 이렇게 계속 중첩이 되다보니까 콜백헬에 빠짐

#

# Promises

비동기 처리의 성공과 실패 결과를 나타내는 객체.

예시로 다른 무비api에서 디비 가져오는걸 많이 한다.

```jsx
makeRequest(
  () => {
    //success 함수
  },
  () => {
    //failure 함수
  }
);
```

요건 콜백형태다. 콜백 두개. 성공하면 첫번째함수, 실패하면 두번째함수 실행

인터넷익스플로러에서 안됨

프로미스형태

결과를 약속하는거다

pending : 미해결의, 보류중인

resolved: 해결된

프로미스 객체가 status로 미해결, 해결, 거부됨 3가지 상태를 보여줌

제이쿼리 ajax 했을때랑 비슷함. 요청성공하면 석세스 함수처리, 아니면 에러함수처리

```jsx
new Promise((resolve, reject) => {
  resoleve();
});
```

```jsx
const fakeRequset = (url) => {
	return new Promise((resolve, reject) => {

```

```java
// THE CLEANEST OPTION WITH THEN/CATCH
// RETURN A PROMISE FROM .THEN() CALLBACK SO WE CAN CHAIN!
fakeRequestPromise('yelp.com/api/coffee/page1')
    .then(() => {
        console.log("IT WORKED!!!!!")
        console.log("Promise resolved!")
		})
		.catch(() => {
				console.log("Promise rejected!")
				console.log("oh no, error!!!")
		})
```

요청은 따로 변수에 담을 필요 없음. 이렇게 들어온 요청을 처리하는데 결과에 따라서 성공이면 프로미스 객체의 함수인 .then() 메소드에 성공 콜백함수를 넣고, 실패할 경우는 .catch() 메소드에 실패 콜백함수를 넣는다.

쉽게 체이닝도 가능하다

```java
fakeRequestPromise('yelp.com/api/coffee/page1')
    .then(() => {
        console.log("IT WORKED!!!!!! (page1)")
        fakeRequestPromise('yelp.com/api/coffee/page2')
            .then(() => {
                console.log("IT WORKED!!!!!! (page2)")
                fakeRequestPromise('yelp.com/api/coffee/page3')
                    .then(() => {
                        console.log("IT WORKED!!!!!! (page3)")
                    })
                    .catch(() => {
                        console.log("OH NO, ERROR!!! (page3)")
                    })
            })
            .catch(() => {
                console.log("OH NO, ERROR!!! (page2)")
            })
    })
    .catch(() => {
        console.log("OH NO, ERROR!!! (page1)")
    })
```

웁스

개선해보자

```java
// THE CLEANEST OPTION WITH THEN/CATCH
// RETURN A PROMISE FROM .THEN() CALLBACK SO WE CAN CHAIN!
fakeRequestPromise('yelp.com/api/coffee/page1')
    .then((data) => {
        console.log("IT WORKED!!!!!! (page1)")
        console.log(data)
        return fakeRequestPromise('yelp.com/api/coffee/page2')
    })
    .then((data) => {
        console.log("IT WORKED!!!!!! (page2)")
        console.log(data)
        return fakeRequestPromise('yelp.com/api/coffee/page3')
    })
    .then((data) => {
        console.log("IT WORKED!!!!!! (page3)")
        console.log(data)
    })
    .catch((err) => {
        console.log("OH NO, A REQUEST FAILED!!!")
        console.log(err)
    })
```

중첩할 필요없이 다음에 실행할 요청을 리턴하고 거기에 체이닝 걸어주면됨

에러를 마지막에 한꺼번에 처리

우리가 프로미스를 실제로 만드는일은없다

그냥 메소드를 사용할뿐이야.

근데 프로미스가 어떻게 만들어져있는지 아는건 좋아

# Async

신택트 슈가

어싱크랑 어웨이트는 같이쓰임

깔끔하게해줌

함수앞에 어싱크 키워드 붙이면 자동으로 프로미스로 리턴됨

```java
const sing = async () => {
  return "LA LA lA lA";
};

sing().then(() => {
  throw new Error("ahhhhh!!");
  console.log("promise resolved with:", data);
});
```

에러를 throw 할 수 있어. throw 키워드 뒤에 그냥 스트링을 써도된다

```java
const sing = async () => {
  return "LA LA lA lA";
};

sing()
  .then(() => {
    console.log("promise resolved with:", data);
  })
  .catch((err) => {
    console.log("oh no, promise rejected!");
    console.log(err);
  });
```

```java
const login = async (username, password) => {
  if (!username || !password) throw "Missing Credentials";
  if (password === "corgifieetarecute") return "WELCOME!";
  throw "Invalid Password";
};

login("mimi", "corgifieetarecute")
  .then((msg) => {
    console.log("logged in!");
    console.log(msg);
  })
  .catch((err) => {
    console.log("error!");
    console.log(err);
  });
```

# Await

이거쓰면 어싱크 함수 실행을 멈춰주고, 다시 실행되기 전에 프로미스가 리졸브 될 수 있도록 기다린다. 어싱크 함수에만 쓸수있어. 짝꿍임

```java
async function rainbow() {
    await delayedColorChange('red', 1000)
    await delayedColorChange('orange', 1000)
    await delayedColorChange('yellow', 1000)
    await delayedColorChange('green', 1000)
    await delayedColorChange('blue', 1000)
    await delayedColorChange('indigo', 1000)
    await delayedColorChange('violet', 1000)
    return "ALL DONE!"
}
```

어웨이트 걸어놓으면 앞에 있는게 끝나야 뒤에있는걸 실행해준다.

```java
// rainbow().then(() => console.log("END OF RAINBOW!"))

async function printRainbow() {
    await rainbow();
    console.log("END OF RAINBOW!")
}
```

저 7초간의 무지개 컬러 실행이 끝나면 요걸 출력해줌

리젝션 핸들링은?

```java
const fakeRequest = (url) => {
    return new Promise((resolve, reject) => {
        const delay = Math.floor(Math.random() * (4500)) + 500;
        setTimeout(() => {
            if (delay > 2000) {
                reject('Connection Timeout :(')
            } else {
                resolve(`Here is your fake data from ${url}`)
            }
        }, delay)
    })
}

async function makeTwoRequests() {
    try {
        let data1 = await fakeRequest('/page1');
        console.log(data1);
        let data2 = await fakeRequest('/page2');
        console.log(data2);
    } catch (e) {
        console.log("CAUGHT AN ERROR!")
        console.log("error is:", e)
    }

}
```

try~catch 에러잡기
