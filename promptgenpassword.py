import streamlit as st

def generate_prompts(product_name, product_description, target_market, product_price):
  prompts = [
      f"1. Create a marketing slogan for {product_name}, a {product_description}, targeting {target_market}.",
      f"2. Write a product description for {product_name}, emphasizing its benefits for {target_market}.",
      f"3. Generate a social media post promoting {product_name}, priced at {product_price}, to {target_market}.",
      f"4. Suggest 5 unique selling points for {product_name}, a {product_description}, for {target_market}.",
      f"5. Write an email campaign introducing {product_name} to {target_market}, highlighting its price of {product_price}.",
      f"6. Create a list of 10 potential blog post titles about {product_name} for {target_market}.",
      f"7. Generate a script for a 30-second advertisement for {product_name}, targeting {target_market}.",
      f"8. Write a press release announcing the launch of {product_name}, a {product_description}, priced at {product_price}.",
      f"9. Suggest ways to improve the packaging of {product_name} to appeal to {target_market}.",
      f"10. Generate a list of 5 influencers who could promote {product_name} to {target_market}."
  ]
  return prompts


def main():
  st.title("Product Prompt Generator")

  # Message on the left-hand side
  st.sidebar.markdown("To receive more free apps for AUTOMATIC prompt generation for all aspects of your startup or business, please send an email to peter.sheceo@gmail.com.")

  if 'password_entered' not in st.session_state:
    st.session_state.password_entered = False

  if not st.session_state.password_entered:
    password = st.text_input("Password:", type="password")
    if st.button("Enter"):
      if password == "superpeter":
        st.session_state.password_entered = True
        st.success("Welcome! 😊")
        st.rerun()  # Changed from experimental_rerun() to rerun()
      else:
        st.error("Incorrect password.")
    return  # Stop execution if password not entered

  # Password is correct, proceed with the app

  # Initialize session state for prompts
  if 'all_prompts' not in st.session_state:
    st.session_state.all_prompts = []

  # Input fields
  product_name = st.text_input("Product Name:")
  product_description = st.text_input("Describe the product in 25 words:")
  target_market = st.text_input("Describe the target market in 25 words:")
  product_price = st.text_input("Product Price:")

  # Generate prompts
  if st.button("Generate Prompts"):
    if all([product_name, product_description, target_market, product_price]):
      new_prompts = generate_prompts(product_name, product_description, target_market, product_price)
      st.session_state.all_prompts.extend(new_prompts)
      st.success("10 prompts generated and added to prompts.txt!")
    else:
      st.error("Please fill in all fields.")

  # Display download button if prompts exist
  if st.session_state.all_prompts:
    # Create downloadable text
    prompt_text = "\n\n".join(st.session_state.all_prompts)

    # Download button
    st.download_button(
      label="Download prompts.txt",
      data=prompt_text,
      file_name="prompts.txt",
      mime="text/plain"
    )

    # Display preview
    st.subheader("Preview of prompts.txt")
    st.text(prompt_text[:1000] + ("..." if len(prompt_text) > 1000 else ""))


if __name__ == "__main__":
  main()
