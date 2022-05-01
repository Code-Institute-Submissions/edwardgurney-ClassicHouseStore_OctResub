
// This is your test publishable API key.
const stripeKey = JSON.parse(document.getElementById('stripe-id').textContent)
console.log(stripeKey)
const bagId = JSON.parse(document.getElementById('bag-id').textContent)
const clientSecret = JSON.parse(document.getElementById('client-secret').textContent)
const returnUrl = JSON.parse(document.getElementById('return-url').textContent)
console.log(returnUrl)
console.log("returnUrl")
//const stripe = Stripe("pk_test_51KpqTKKMum47C0L1yixvLLYq2k4F53azrv5KoWQNCa6y68bFHCx4tAYFE4CzugAEAX3AX1D7jG8bmrm4EKWhSqKM00YVzWkcsR");
const stripe = Stripe(stripeKey)
// The items the customer wants to buy

let elements;

initialize();
checkStatus();
console.log(document.querySelector("#payment-form"))

// Fetches a payment intent and captures the client secret
async function initialize() {
 // const response = await fetch(`/create-payment-intent/${bagId}`, {
 //   method: "GET",
 //   // headers: { "Content-Type": "application/json" },
 //   body: JSON.stringify(),
 // });
 // const { clientSecret } = await response.json();
 // console.log(clientSecret)

 const appearance = {
   theme: 'stripe',
 };
 elements = stripe.elements({ appearance, clientSecret });

 const paymentElement = elements.create("payment");
 paymentElement.mount("#payment-element");
}

async function handleSubmit(e) {
 e.preventDefault();
 setLoading(true);

 console.log(returnUrl)

 const { error } = await stripe.confirmPayment({
   elements,
   confirmParams: {
     // Make sure to change this to your payment completion page
     return_url: `https://8000-edwardgurney-classichous-ulqtny37znu.ws-eu43.gitpod.io${returnUrl}`
     // return_url: `${returnUrl}`,

   },
 });
 console.log(error)
 // This point will only be reached if there is an immediate error when
 // confirming the payment. Otherwise, your customer will be redirected to
 // your `return_url`. For some payment methods like iDEAL, your customer will
 // be redirected to an intermediate site first to authorize the payment, then
 // redirected to the `return_url`.
 if (error.type === "card_error" || error.type === "validation_error") {
   showMessage(error.message);
 } else {
   showMessage("An unexpected error occured.");
 }

 setLoading(false);
}
document
.querySelector("#payment-form")
.addEventListener("submit", handleSubmit);

// Fetches the payment intent status after payment submission
async function checkStatus() {
 const clientSecret = new URLSearchParams(window.location.search).get(
   "payment_intent_client_secret"
 );

 if (!clientSecret) {
   return;
 }

 const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

 switch (paymentIntent.status) {
   case "succeeded":
     showMessage("Payment succeeded!");
     break;
   case "processing":
     showMessage("Your payment is processing.");
     break;
   case "requires_payment_method":
     showMessage("Your payment was not successful, please try again.");
     break;
   default:
     showMessage("Something went wrong.");
     break;
 }
}

// ------- UI helpers -------

function showMessage(messageText) {
 const messageContainer = document.querySelector("#payment-message");

 messageContainer.classList.remove("hidden");
 messageContainer.textContent = messageText;

 setTimeout(function () {
   messageContainer.classList.add("hidden");
   messageText.textContent = "";
 }, 4000);
}

// Show a spinner on payment submission
function setLoading(isLoading) {
 if (isLoading) {
   // Disable the button and show a spinner
   document.querySelector("#submit").disabled = true;
   document.querySelector("#spinner").classList.remove("hidden");
   document.querySelector("#button-text").classList.add("hidden");
 } else {
   document.querySelector("#submit").disabled = false;
   document.querySelector("#spinner").classList.add("hidden");
   document.querySelector("#button-text").classList.remove("hidden");
 }
}
