<template>
  <div class="market-page">
    <!-- Posts Container -->
    <div class="posts-container grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      <div v-for="(post, index) in posts" :key="index" class="post-item relative group">
        <!-- Image Grid -->
        <div v-if="post.imageUrl" class="post-image-grid h-64">
          <img class="w-full h-full object-cover" :src="post.imageUrl" alt="Post image" />
        </div>

        <!-- Title and Business Name placed BELOW the square image -->
        <div class="mt-2">
          <h3 class="post-title text-lg font-semibold text-gray-800 text-center">
            {{ post.title }} <span class="text-sm text-gray-600">- {{ post.businessName }}</span>
          </h3>
        </div>

        <!-- Delete and Edit Buttons on hover -->
        <div class="absolute top-2 right-2 space-x-2 opacity-0 group-hover:opacity-100 transition-opacity">
          <button
            @click="editPost(index)"
            class="bg-blue-500 text-white py-1 px-3 rounded"
          >
            Edit
          </button>
          <button
            @click="deletePost(index)"
            class="bg-red-500 text-white py-1 px-3 rounded"
          >
            Delete
          </button>
        </div>
      </div>
    </div>

    <!-- Floating button to create a new post -->
    <button @click="toggleCreateForm" class="floating-add-button fixed bottom-5 right-5 bg-green-500 text-white text-2xl w-12 h-12 rounded-full shadow-lg">+</button>

    <!-- Modal to create/edit a post -->
    <div v-if="showForm" class="modal fixed inset-0 bg-gray-900 bg-opacity-50 flex justify-center items-center">
      <div class="modal-content p-6 text-color=gray rounded-lg shadow-lg w-96">
        <span class="close cursor-pointer text-xl" @click="toggleCreateForm">&times;</span>
        <h2 class="text-xl font-bold mb-4">{{ isEditing ? 'Edit Post' : 'Create a New Post' }}</h2>
        <form @submit.prevent="isEditing ? updatePost() : addPost()">
          <div class="form-group mb-4">
            <label for="title" class="block mb-2">Title:</label>
            <input type="text" id="title" v-model="newPost.title" class="w-full text-black border p-2 rounded" required />
          </div>
          <div class="form-group mb-4">
            <label for="businessName" class="block mb-2">Business Name:</label>
            <input type="text" id="businessName" v-model="newPost.businessName" class="w-full text-black border p-2 rounded" required />
          </div>
          <div class="form-group mb-4">
            <label for="content" class="block mb-2">Content:</label>
            <textarea id="content" v-model="newPost.content" class="w-full text-black border p-2 rounded" required></textarea>
          </div>
          <div class="form-group mb-4">
            <label for="image" class="block mb-2">Image:</label>
            <input type="file" id="image" @change="onImageChange" class="w-full border p-2 rounded" />
          </div>
          <button type="submit" class="w-full bg-green-500 text-white py-2 rounded">{{ isEditing ? 'Update Post' : 'Add Post' }}</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showForm: false,
      isEditing: false,
      editingIndex: null,
      newPost: {
        title: "",
        businessName: "",  // Add business name to newPost data model
        content: "",
        imageUrl: null
      },
      posts: []
    };
  },
  created() {
    this.loadPosts();
  },
  methods: {
    toggleCreateForm() {
      this.showForm = !this.showForm;
      if (!this.showForm) {
        this.resetForm();
      }
    },
    resetForm() {
      this.newPost = { title: "", businessName: "", content: "", imageUrl: null };
      this.isEditing = false;
      this.editingIndex = null;
    },
    addPost() {
      if (this.newPost.title && this.newPost.content && this.newPost.businessName) {
        this.posts.push({ ...this.newPost });
        this.resetForm();
        this.showForm = false;
        this.savePosts();
      }
    },
    editPost(index) {
      this.newPost = { ...this.posts[index] };
      this.isEditing = true;
      this.editingIndex = index;
      this.showForm = true;
    },
    updatePost() {
      if (this.newPost.title && this.newPost.content && this.newPost.businessName) {
        this.posts[this.editingIndex] = { ...this.newPost };
        this.resetForm();
        this.showForm = false;
        this.savePosts();
      }
    },
    deletePost(index) {
      this.posts.splice(index, 1);
      this.savePosts();
    },
    onImageChange(event) {
      const file = event.target.files[0];
      if (file) {
        const imageUrl = URL.createObjectURL(file);
        this.newPost.imageUrl = imageUrl;
      }
    },
    savePosts() {
      try {
        const postString = JSON.stringify(this.posts);
        localStorage.setItem("posts", postString);
      } catch (error) {
        console.error("LocalStorage issue:", error);
      }
    },
    loadPosts() {
      const savedPosts = localStorage.getItem("posts");
      if (savedPosts) {
        this.posts = JSON.parse(savedPosts);
      }
    }
  }
};
</script>

<style scoped>
.post-item {
  background-color:white ;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
  position: relative;
}

.post-item:hover {
  transform: scale(1.02);
}

.post-image-grid {
  position: relative;
  width: 100%;
}

.post-image-grid img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.post-title {
  margin-top: 10px;
  text-align: center;
}

.modal-content {
  position: relative;
}

.close {
  position: absolute;
  top: 0;
  right: 0;
}

.group:hover .delete-button {
  opacity: 1; /* Show delete button on hover */
}
</style>
