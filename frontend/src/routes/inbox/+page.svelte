<script>

    // Later implement a feature that if there is no messsage, it will show a message saying "No notifications yet"
    
    // Track whether the dropdown is open or closed
    let isOpen = $state(false);
    
    // Store reference to the dropdown button wrapper element
    let menuContainer;
</script>

<!-- Inline the handler to fix the ESLint unused-variable error -->
<svelte:window onclick={(e) => {
    if (isOpen && menuContainer && !menuContainer.contains(e.target)) {
        isOpen = false;
    }
}} />


<div class="flex justify-center text-3xl font-bold mt-5">
    <h1>Inbox</h1>
</div>

<div class="flex min-h-dvh justify-center items-start">

    <!-- Container -->
    <div class="bg-gray-200 p-5 rounded-2xl w-full max-w-5xl mt-5 mb-10">
        <ul class="space-y-3">

            <!-- Message Row 1 -->
            <li class="flex items-center justify-between gap-6 bg-white p-4 rounded-xl shadow-sm">
                <!-- Left Column: Profile & Name Stack -->
                <div class="flex flex-col items-center justify-center shrink-0 w-20 text-center">
                    <div class="w-12 h-12 bg-gray-300 rounded-full flex items-center justify-center font-bold text-gray-600 text-sm">
                        JD
                    </div>
                    <span class="text-xs font-semibold text-gray-700 mt-1 truncate w-full">John Smith</span>
                </div>
                <!-- Middle Column: Message Text -->
                <div class="flex-1 min-w-0">
                    <p class="text-gray-800 text-base leading-relaxed">
                        Message 1: This is the main body text of your notification message. It stretches across the middle of the container. More message here to test things out.
                    </p>
                </div>
                <!-- Right Column: 3-Dots Dropdown Button & Menu Button with Dropdown Container-->
                <div class="relative shrink-0" bind:this={menuContainer}> 
                    
                    <!-- Meatball Button (Toggles state) -->
                    <button 
                        type="button" 
                        onclick={() => isOpen = !isOpen}
                        class="p-2 hover:bg-gray-100 rounded-full transition-colors text-gray-600 hover:text-gray-900" 
                        aria-expanded={isOpen}
                        aria-label="More options">

                        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M6 10c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm12 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-6 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                        </svg>
                    </button>

                    <!-- Dropdown Menu Box -->
                    {#if isOpen}
                        <div class="absolute right-0 top-full mt-2 w-48 rounded-xl border border-gray-100 bg-white p-1.5 shadow-xl z-10">
                            <div class="flex flex-col gap-0.5" role="menu">
                                <button type="button" class="flex w-full items-center rounded-lg px-3 py-2 text-left text-sm text-gray-700 hover:bg-gray-50 transition-colors" role="menuitem">
                                    Operation 1
                                </button>

                                <button type="button" class="flex w-full items-center rounded-lg px-3 py-2 text-left text-sm text-gray-700 hover:bg-gray-50 transition-colors" role="menuitem">
                                    Operation 2
                                </button>
                                
                                <button type="button" class="flex w-full items-center rounded-lg px-3 py-2 text-left text-sm text-red-600 hover:bg-red-50 transition-colors" role="menuitem">
                                    Delete message
                                </button>
                            </div>
                        </div>
                    {/if}

                </div>
            </li>

            

        </ul>
    </div>

</div>

<style>

</style>